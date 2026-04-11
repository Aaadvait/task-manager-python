from customtkinter import *
from gui.global_gui import *

class ManageSubjectFrame():
    def __init__(self, parent):
        self.managesubject_frame = CTkFrame(parent,
                                        fg_color=C_PAGE,
                                        corner_radius=0)
        self.managesubject_frame.grid(row=0, column=0, sticky='nsew')

    def destroy_gui(self):
        self.managesubject_frame.destroy()