from customtkinter import *
from global_gui import *

class MANAGETASKS_FRAME():
    def __init__(self, parent):
        self.managetask_frame = CTkFrame(parent,
                                        fg_color=color_mainframe,
                                        corner_radius=0)
        self.managetask_frame.grid(row=0, column=0, sticky='nsew')

    def destroy_gui(self):
        self.managetask_frame.destroy()