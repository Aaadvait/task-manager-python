from gui.global_gui import *
from customtkinter import *
from gui.ui_body import BodyFrame


class MainWindow:
    def __init__(self):
        self.window = CTk()

        # Main Window ---
        self.window.title("Task Manager")
        self.window.iconbitmap(main_window_icon)
        self.window.geometry("1280x720")
        #self.window.resizable(False, False)
        self.window.configure(fg_color=C_PAGE)

        # Grid Configuration ---
        self.window.rowconfigure((0, 2), weight=0)
        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(0, weight=1)

        # Body Frame ---
        BodyFrame(self.window)

    def run(self):
        self.window.mainloop()