from Entity.Patient import Patient

import json

class ReadPatient:
    def __init__(self):
        self.patient = Patient()

    def upload(self, path_folder):
        meta_data = path_folder + '/patient.json'
        obsv_data = path_folder + '/obsv/'

        with open(meta_data, 'r') as fcc_file:
            patients_fields = json.loads(json.load(fcc_file).replace("'", "\""))
            self.patient.made_valid_user(
                patients_fields['id'],
                patients_fields['first_name'],
                patients_fields['second_name'],
                patients_fields['comment'],
                patients_fields['age'],
                patients_fields['smoke'],
            )

        # upload observes

    def make_example(self):
        return self.patient.to_numpy()

    def write_res(self, res):
        res = res[0][0]
        if res == 1.0:
            self.patient.write_res(True)
        else:
            self.patient.write_res(False)