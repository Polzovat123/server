import pandas as pd
import numpy as np

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


    def _encode_first_name(self):
        self.first_name = int(123)

    def _encode_second_name(self):
        self.second_name = int(321)

    def _encode_comment(self):
        self.comment = int(222)

    def to_panda(self):
        self._encode_first_name()
        self._encode_second_name()
        self._encode_comment()
        return pd.DataFrame(
            np.array([[self.first_name, self.second_name, self.comment, self.age, self.smoke]]),
            columns=['first_name', 'second_name', 'comment', 'age', 'smoke']
        ).astype({
            'age':  np.float,
            'smoke': 'bool',
            'first_name': np.float,
            'second_name': np.float,
            'comment': np.float,
        }) # should be modify

    def to_numpy(self):
        self._encode_first_name()
        self._encode_second_name()
        self._encode_comment()
        return np.array([
            [
                np.float(self.first_name),
                np.float(self.second_name),
                np.float(self.comment),
                np.float(self.age),
                np.float(self.smoke)
            ]
        ])

    def write_res(self, answer):
        self.result = answer