from data.global_data import *
import pandas as pd

class TaskFileRead():
    def __init__(self):
        self.df = pd.read_csv(taskfile_loc)

    # --- FILTERS ---
    def get_high_priority(self):
        return self.df[
            (self.df["priority"] == 1) &
            (self.df["completion"] == 0)
            ]

    def get_completed(self):
        return self.df[self.df["completion"] == 1]

    def get_remaining(self):
        return self.df[self.df["completion"] == 0]

    # --- SAVE ---
    def save(self):
        self.df.to_csv(taskfile_loc, index=False)