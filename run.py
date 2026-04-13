from gui.main_window import MainWindow
from system.initialize import InitializeFiles
from system.ENDC import ENDC



def main():
    endc = ENDC()
    InitializeFiles()
    app_window = MainWindow()
    app_window.run()
    endc.genrate_files()
main()