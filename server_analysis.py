import owncloud
import zipfile\

import os

def download_analysis_res():
    public_link = 'https://127.0.0.1/index.php/f/198'

    oc = owncloud.Client.from_public_link(public_link)
    oc.login('user', 'user')
    all_files = oc.list('Analysis')
    for file in all_files:
      print(file.path)
      if file.path.find('.') != -1:
         continue
      oc.get_file(file.path, 'res.zip')
      with zipfile.ZipFile('res.zip', 'r') as zip_ref:
        zip_ref.extractall('obs')

def upload_model(path='models/example.pickle'):
   model = []

   return model

def create_and_mark_dataset(model, path_observ='/home/user/projects/obs/home/user/observs'):
   directory = os.listdir(path_observ)
   for folder in directory:
      parser = ReadPatient()
      parser.upload(path_observ+'/'+folder)
      except_preditc = parser.make_example()
      response = model.predict(except_predict)
      fl = FileWorker(self.path)
      fl.save_patient(self.add_user)


if __name__ == '__main__':
    download_analysis_res()
    mdl = upload_model()
    create_and_mark_dataset(mdl)