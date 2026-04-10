from pathlib import Path
from theme import *

BASE_DIR = Path(__file__).resolve().parent.parent
RESOURCES = BASE_DIR / "resources"
DATA = BASE_DIR / "data"

#MAIN WINDOW ICON
main_window_icon = str(RESOURCES / "tm_icon.ico")