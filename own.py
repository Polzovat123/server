import owncloud
import os
from zipfile import ZipFile

path_project = '/home/user/projects/Observs'

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
    if path is None:
        path = path_project
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
    send_folder_to_server(and_train=True)