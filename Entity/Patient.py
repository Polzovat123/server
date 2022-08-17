

class Patient:
    def __init__(self):
        self.id = None
        self.first_name = None
        self.second_name = None
        self.comment = None
        self.age = None
        self.smoke = None
        self.result = None

        self.observations = []

    def made_valid_user(self, id, f_name, s_name, com, age, smoke):
        self.id = id
        self.first_name = f_name
        self.second_name = s_name
        self.comment = com
        self.age = age
        self.smoke = smoke