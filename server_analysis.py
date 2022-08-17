import owncloud
from Adapter.FileWorker import FileWorker
from Adapter.PatinentAdapter import ReadPatient
from keras.layers import Dense
from keras.layers import Input
from keras.models import Model
import tensorflow as tf

import zipfile
import os

def download_analysis_res():
    public_link = 'https://127.0.0.1/index.php/f/198'

    oc = owncloud.Client.from_public_link(public_link)
    oc.login('user', 'user')
    all_files = oc.list('Analysis')
    for file in all_files:
        if file.path.find('.') != -1:
            continue
        oc.get_file(file.path, 'res.zip')
        with zipfile.ZipFile('res.zip', 'r') as zip_ref:
            zip_ref.extractall('obs')

def upload_model(path='model/weight.h5'):
    input_layer = Input((5)) # in orig should be another number
    hidden_layer = Dense(15, activation='relu')(input_layer)
    output_layer = Dense(1, activation='sigmoid')(hidden_layer)

    network = Model(inputs=input_layer, outputs=output_layer)
    network.load_weights(path)
    return network

def create_and_mark_dataset(model, path_observ='obs/home/user/observs'):
    directory = os.listdir(path_observ)
    for folder in directory:
        parser = ReadPatient()
        parser.upload(path_observ+'/'+folder)
        except_predict = parser.make_example()
        response = model.predict(tf.convert_to_tensor(except_predict))
        parser.write_res(response)
        fl = FileWorker('send')
        fl.save_patient(parser.patient)

def send_file_analysis(file_name, names):
    if names.find('zip') != -1:
        return
    oc = owncloud.Client("https://127.0.0.1")
    oc.login("user", "user")
    with ZipFile(file_name + '.zip', 'w') as zipObj:
        directory = os.listdir(file_name)
        for component in directory:
            zipObj.write(file_name+'/'+component)
    print('complete observs')
    oc.put_file(r'Analysis/'+names, file_name + '.zip')

def send_file_train(file_name, names):
    oc = owncloud.Client("https://127.0.0.1")
    oc.login("user", "user")
    if names.find('zip') != -1:
            return
    with ZipFile(file_name + '.zip', 'w') as zipObj:
        directory = os.listdir(file_name)
        for component in directory:
            zipObj.write(file_name+'/'+component)
    oc.put_file(r'TrainSet/'+names, file_name + '.zip')

def send_folder_to_server(path=None, and_train=False):
    directory = os.listdir(path)
    print(directory)
    for file in directory:
        send_file_analysis(path+r'/'+file, file)
    if and_train:
        for file in directory:
            send_file_train(path + r'/' + file, file)

def clear_memory(path=None):
    if path is None:
        path = path_project
    directory = os.listdir(path)
    for file in directory:
        os.remove(path+r'/'+file)

if __name__ == '__main__':
    download_analysis_res()
    mdl = upload_model()
    create_and_mark_dataset(mdl)
    send_folder_to_server(path='send', and_train=True)