from data.global_data import *
from pathlib import Path


def tsum_generate(file_name, file_tsum):
    file_name_loc = Path(file_name)
    if not file_name_loc.exists():
        raise Exception(f"File {file_name} not found")

    with open(file_name, "r") as FileMain:
        with open(file_tsum, "w") as FileTSUM:
            while True:
                sum_val = 0
                line_val=FileMain.readline().rstrip("\n")
                if line_val == "":
                    break
                for i in line_val:
                    sum_val += ord(i)
                FileTSUM.write(f"{sum_val}\n")

def backup_generate(file_name, file_bak):
    file_name_loc = Path(file_name)
    if not file_name_loc.exists():
        raise Exception(f"File {file_name} not found")

    with open(file_name, "r") as FileMain:
        with open(file_bak, "w") as FileTemp:
            while True:
                line_val = FileMain.readline()
                if line_val == "":
                    break
                FileTemp.write(line_val)


def tsum_check(file_name, file_tsum):
    file_name_loc = Path(file_name)
    if not file_name_loc.exists():
        raise Exception(f"File {file_name} not found")
    file_tsum_loc = Path(file_name)
    if not file_tsum_loc.exists():
        raise Exception(f"File {file_tsum} not found")

    with open(file_name) as FileMain:
        with open(file_tsum) as FileTSUM:
            while True:
                tsum = 0
                line_value = FileMain.readline().rstrip("\n")
                if line_value == "":
                    break
                sum_value = int(FileTSUM.readline().rstrip("\n"))
                for i in line_value:
                    tsum += ord(i)
                if not (tsum == sum_value):
                    return True
    return False

def tsum_correct(file_name, file_tsum, file_bak):
    file_name_loc = Path(file_name)
    if not file_name_loc.exists():
        raise Exception(f"File {file_name} not found")
    file_tsum_loc = Path(file_tsum)
    if not file_tsum_loc.exists():
        raise Exception(f"File {file_tsum} not found")
    file_bak_loc = Path(file_bak)
    if not file_bak_loc.exists():
        raise Exception(f"File {file_bak} not found")

    # Make a TEMP file from the backup and Main file
    with open(file_name) as FileMain:
        with open(file_tsum) as FileTSUM:
            with open(file_bak) as FileBak:
                with open("temp", "w") as FileTemp:
                    while True:
                        tsum = 0
                        line_value = FileMain.readline().rstrip("\n")
                        skip_value = FileBak.readline().rstrip("\n")
                        if line_value == "":
                            break
                        sum_value = int(FileTSUM.readline().rstrip("\n"))
                        for i in line_value:
                            tsum += ord(i)
                        if not (tsum == sum_value):
                            FileTemp.write(skip_value+"\n")
                        else:
                            FileTemp.write(line_value+"\n")

    # Substitue the Temp file inside the Main file
    with open(file_name, "w") as FileMain:
        with open("temp") as FileTemp:
            while True:
                line_value = FileTemp.readline()
                if line_value == "":
                    break
                FileMain.write(line_value)


class ENDC:
    def __init__(self):

        # --- Generating file location lists --------------------
        self.files = [subject_file_loc, taskfile_loc]
        self.files_bak = [(x+".bak") for x in self.files]
        self.files_tsum = [(x+".tsum") for x in self.files]

        # --- Initializing Variables --------------------
        self.file_error_state = [False,False]
        self.first_time = False

        self.file_check()
        if not self.first_time:
            self.error_check()
            self.error_correct()

    def file_check(self):
        for y in self.files_bak:
            file_loc = Path(y)
            if not file_loc.exists():
                temp_var = open(y, "w")
                self.first_time = True
                temp_var.close()
        for z in self.files_tsum:
            file_loc = Path(z)
            if not file_loc.exists():
                temp_var = open(z, "w")
                self.first_time = True
                temp_var.close()

    def genrate_files(self):
        """Exit state. This is called at the end of all programs to save data"""
        tsum_generate(self.files[0], self.files_tsum[0])
        tsum_generate(self.files[1], self.files_tsum[1])
        backup_generate(self.files[0], self.files_bak[0])
        backup_generate(self.files[1], self.files_bak[1])

    def error_check(self):
        self.file_error_state[0] = tsum_check(self.files[0], self.files_tsum[0])
        self.file_error_state[1] = tsum_check(self.files[1], self.files_tsum[1])

    def error_correct(self):
        if self.file_error_state[0]:
            tsum_correct(self.files[0], self.files_tsum[0], self.files_bak[0])
        if self.file_error_state[1]:
            tsum_correct(self.files[1], self.files_tsum[1], self.files_bak[1])

        self.genrate_files()