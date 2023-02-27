import pandas as pd
from os.path import exists


class OutputFile():
    def __init__(self, path_to_out_file, path_to_hist_table):
        self.path_to_out_file = path_to_out_file

        self.columns = ['false_reject', 'false_match',
                        'unrecognizable',
                        'poor_brightness', 'poor_contrast', 'poor_focus',
                        'poor_angle',
                        'spoofing',
                        'comment'
                        ]

        if not exists(self.path_to_out_file):
            self.create_out_file(path_to_hist_table)
        else:
            self.df = pd.read_csv(self.path_to_out_file)

    def create_out_file(self, path_to_hist_table):
        self.df = pd.read_csv(path_to_hist_table)

        for column in self.columns:
            self.df[column] = None

        self.save_to_file()

    def update(self, index, key, val):
        self.df[key][index] = val

    def save_to_file(self):
        self.df.to_csv(self.path_to_out_file, index=False)
