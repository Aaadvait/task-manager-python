from data.global_data import *
from datetime import date
import pandas as pd

today = date.today()
f_today = today.strftime("%d-%m-%Y")


class TaskFileRead():
    def __init__(self):
        self.df = pd.read_csv(taskfile_loc)
        self.sf = pd.read_csv(subject_file_loc)

    # ----- ADD TASK -------------------------

    def add_task(self, date, priority, completion, subject, tasktype, taskno, taskdisc):
        subject = subject.strip()
        tasktype = tasktype.strip()
        taskno = int(taskno)

        mask = (
                (self.df["subject"] == subject) &
                (self.df["tasktype"] == tasktype) &
                (self.df["taskno"] == taskno)
        )
        if mask.any():
            raise Exception("Duplicate Task: same subject, type, and task number already exists")

        new_row = pd.DataFrame([{
            "date": date,
            "priority": int(priority),
            "completion": int(completion),
            "subject": subject,
            "tasktype": tasktype,
            "taskno": taskno,
            "taskdisc": taskdisc.strip()
        }])

        self.df = pd.concat([self.df, new_row], ignore_index=True)
        self.save()

    # ----- Get Data from the file -------------------------

    def refresh_dataframe(self):
        self.df = pd.read_csv(taskfile_loc)

    def get_high_priority(self):
        return self.df[(self.df["priority"] == 1) &
                       (self.df["completion"] == 0)
        ]

    def get_today(self):
        return self.df[(self.df["date"] == f_today) &
                       (self.df["completion"] == 0)
        ]

    def get_overdue(self):
        return self.df[(self.df["date"] < f_today) &
                       (self.df["completion"] == 0)
        ]

    def get_completed(self):
        return self.df[self.df["completion"] == 1]

    def get_remaining(self):
        return self.df[self.df["completion"] == 0]

    # --- Get Subjects ------------

    def refresh_subject_list(self):
        self.sf = pd.read_csv(subject_file_loc)

    def add_subject(self, subject):
        subject = subject.strip()

        if subject == "":
            raise Exception("Subject cannot be empty")

        if subject in self.sf["subject"].values:
            raise Exception("Subject already exists")

        new_row = pd.DataFrame({"subject": [subject]})
        self.sf = pd.concat([self.sf, new_row], ignore_index=True)

        self.sf.to_csv(subject_file_loc, index=False)

    def rename_subject(self, old, new):
        new = new.strip()

        if new == "":
            raise Exception("Subject cannot be empty")

        if new in self.sf["subject"].values:
            raise Exception("Subject already exists")

        if old not in self.sf["subject"].values:
            raise Exception("Subject not found")

        self.sf.loc[self.sf["subject"] == old, "subject"] = new
        self.sf.to_csv(subject_file_loc, index=False)

        self.df.loc[self.df["subject"] == old, "subject"] = new
        self.save()

    def delete_subject(self, subject):
        if subject not in self.sf["subject"].values:
            raise Exception("Subject not found")

        self.sf = self.sf[self.sf["subject"] != subject].reset_index(drop=True)
        self.sf.to_csv(subject_file_loc, index=False)

        self.df = self.df[self.df["subject"] != subject].reset_index(drop=True)
        self.save()

    # --- SAVE ---
    def save(self):
        self.df.to_csv(taskfile_loc, index=False)