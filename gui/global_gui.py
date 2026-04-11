from pathlib import Path
from gui.theme import *

BASE_DIR = Path(__file__).resolve().parent.parent
RESOURCES = BASE_DIR / "resources"

#MAIN WINDOW ICON
main_window_icon = str(RESOURCES / "tm_icon.ico")
delete_cross_icon = str(RESOURCES / "delete.ico" )