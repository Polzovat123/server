import os
import json

class FileWorker:
    def __init__(self, path):
        self.parent_dir = path

    def save_patient(self, patient):
        if patient.id is None or len(patient.id) < 1:
            return
        directory = str(patient.id)
        new_path = os.path.join(self.parent_dir, directory)
        if not os.path.isfile(new_path):
            os.makedirs(new_path)
        print(new_path)

        meta_info_patient = json.dumps(patient.__dict__)
        with open(new_path + '/patient.json', 'w') as outfile:
            json.dump(meta_info_patient, outfile)

    def write_result_cancer(self, patient):
        if patient.id is None or len(patient.id) < 1:
            return
        directory = str(patient.id)
        new_path = os.path.join(self.parent_dir, directory)
        if not os.path.isdir(new_path):
            return
        with open(new_path+'/result.txt', 'w') as f:
            f.write(str())