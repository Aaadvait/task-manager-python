from customtkinter import *
from global_gui import *

class DASHBOARD_FRAME():
    def __init__(self, parent):

        self.pad_value = 20

        self.dashboard_frame = CTkFrame(parent,
                                        fg_color=color_mainframe,
                                        corner_radius=0)
        self.dashboard_frame.grid(row=0, column=0, sticky='nsew')
        self.dashboard_frame.rowconfigure(0, weight=1)
        self.dashboard_frame.rowconfigure(1, weight=4)
        self.dashboard_frame.columnconfigure(0, weight=1)

        self.summary_frame = CTkFrame(self.dashboard_frame, fg_color="blue")
        self.summary_frame.grid(row=0, column=0, sticky='nsew', padx=self.pad_value, pady=self.pad_value)

        self.tasklist_frame = CTkFrame(self.dashboard_frame, fg_color="green")
        self.tasklist_frame.grid(row=1, column=0, sticky='nsew', padx=self.pad_value, pady=self.pad_value)

    def destroy_gui(self):
        self.dashboard_frame.destroy()