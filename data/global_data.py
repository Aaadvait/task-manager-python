from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA = BASE_DIR / "data"

taskfile_name = "tasks.csv"
taskfile_loc = str(DATA / taskfile_name)

cfile_name = "completed.csv"
cfile_loc = str(DATA/ cfile_name)

change_file_name = "change.csv"
change_file_loc = str(DATA / change_file_name)
