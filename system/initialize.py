from data.global_data import *
from pathlib import Path

# Checks if files are present for the functioning of the task manager
# If they are not, it will create them

class InitializeFiles:
    def __init__(self):

        self.file_path_tasks_csv = Path(taskfile_loc)
        self.file_path_subjs_csv = Path(subject_file_loc)

        self._check_task_csv()
        self._check_subj_csv()

    def _check_subj_csv(self):
        if self.file_path_subjs_csv.exists():
            print(f"Found: {self.file_path_subjs_csv}")
        else:
            print(f"Not Found: {self.file_path_subjs_csv}")
            print("Creating File")
            subjs_csv = open(self.file_path_subjs_csv, "w")
            subjs_csv.write("subject\n")
            subjs_csv.close()
            print(f"Created: {self.file_path_subjs_csv}")

    def _check_task_csv(self):

        if self.file_path_tasks_csv.exists():
            print(f"Found: {self.file_path_tasks_csv}")
        else:
            print(f"Not Found: {self.file_path_tasks_csv}")
            print("Creating File")
            tasks_csv = open(self.file_path_tasks_csv, "w")
            tasks_csv.write("date,priority,completion,subject,tasktype,taskno,taskdisc\n")
            tasks_csv.close()
            print(f"Created: {self.file_path_tasks_csv}")
