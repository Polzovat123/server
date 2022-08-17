import json

class ReadPatient:
    def __init__(self):
        self.patient = Patient()

    def upload(self, path_folder):
        meta_data = path_folder + '/patient.json'
        obsv_data = path_folder + '/obsv/'

        with open(meta_data, 'r') as fcc_file:
            patients_fields = json.load(fcc_file)
            # push patient fields in patient

        # upload observes

    def make_example(self):
        # make panda row
        return self.patient