from customtkinter import *
from global_gui import *

class MANAGESUBJECT_FRAME():
    def __init__(self, parent):
        self.managesubject_frame = CTkFrame(parent,
                                        fg_color=color_mainframe,
                                        corner_radius=0)
        self.managesubject_frame.grid(row=0, column=0, sticky='nsew')

    def destroy_gui(self):
        self.managesubject_frame.destroy()