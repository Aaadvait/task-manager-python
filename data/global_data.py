from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA = BASE_DIR / "data"
FILE = BASE_DIR / "files"

taskfile_name = "tasks.csv"
taskfile_loc = str(FILE / taskfile_name)

cfile_name = "completed.csv"
cfile_loc = str(FILE/ cfile_name)

subject_file_name = "subject_file.csv"
subject_file_loc = str(FILE / subject_file_name)
