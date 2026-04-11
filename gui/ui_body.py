from gui.global_gui import *
from customtkinter import *
from gui.dashboard_gui import DashboardFrame
from gui.managetask_gui import ManageTasksFrame
from gui.managesubject_gui import ManageSubjectFrame

from data.task_read import TaskFileRead

class BodyFrame:

    def __init__(self, parent):

        self.active_frame = "DB" #DB, MT, MS
        self.frame_class = None
        self.parent = parent

        self.btn_cnr = 10
        self.btn_width = 240
        self.active_text = color_4
        self.muted_text = color_3
        self.active_color = color_5a
        self.idle_color = color_5

        # CONFIGURING BODY FRAME
        self.body_frame = CTkFrame(self.parent, corner_radius=0, fg_color=color_base)
        self.body_frame.grid(row=1, column=0, sticky='nsew')

        self.body_frame.rowconfigure(0, weight=1)
        self.body_frame.columnconfigure(0, weight=1)  # SIDEBAR
        self.body_frame.columnconfigure(1, weight=100)  # MAINSECTION

        #Creating MainFrame
        self.mainframe = CTkFrame(self.body_frame,
                                  corner_radius=0,
                                  fg_color=color_base)
        self.mainframe.grid(row=0, column=1, sticky='nsew')
        self.mainframe.rowconfigure(0,weight=1)
        self.mainframe.columnconfigure(0, weight=1)

        #Creating Sidebar
        self.sidebar = CTkFrame(self.body_frame,
                                corner_radius=0,
                                fg_color=color_hbase)
        self.sidebar.grid(row=0, column=0, sticky='nsew')

        self.sidebar_width = CTkFrame(self.sidebar, corner_radius=0, fg_color=color_hbase, width=320, height=0)
        self.sidebar_width.pack(side="bottom")

        self.sidebar_divider = CTkFrame(self.sidebar,
                                        corner_radius=0,
                                        fg_color=color_5a,
                                        width=2)
        self.sidebar_divider.pack(side="right", fill="y")

        self.sidebar_label = CTkLabel(self.sidebar,
                                      text="⚙️ Controls",
                                      font=("Bungee", 18),
                                      bg_color=color_5a,
                                      text_color=self.muted_text)
        self.sidebar_label.pack(pady=10, fill='both')

        self.sidebar_motif = CTkLabel(self.sidebar,
                                      text="🕒 Stay Consistent 🕜",
                                      font=("Bungee", 18),
                                      text_color=self.muted_text)
        self.sidebar_motif.pack(side="bottom")

        #BUTTONS!!!

        self.dashboard_button=CTkButton(self.sidebar,
                                        text="Dash Board",
                                        font=("Bungee", 14),
                                        text_color=self.active_text,
                                        corner_radius=self.btn_cnr,
                                        fg_color=self.idle_color,
                                        hover_color=self.active_color,
                                        border_width=1,
                                        border_color=color_hhbase,
                                        width=self.btn_width,
                                        command=self.click_dashboard)
        self.dashboard_button.pack(pady=10)

        self.managetask_button = CTkButton(self.sidebar,
                                          text="Manage Tasks",
                                          font=("Bungee", 14),
                                          text_color=self.active_text,
                                          corner_radius=self.btn_cnr,
                                          fg_color=self.idle_color,
                                          hover_color=self.active_color,
                                          border_width=1,
                                          border_color=color_hhbase,
                                          width=self.btn_width,
                                          command=self.click_managetask)
        self.managetask_button.pack(pady=10)

        self.managesubject_button = CTkButton(self.sidebar,
                                          text="Manage Subjects",
                                          font=("Bungee", 14),
                                          text_color=self.active_text,
                                          corner_radius=self.btn_cnr,
                                          fg_color=self.idle_color,
                                          hover_color=self.active_color,
                                          border_width=1,
                                          border_color=color_hhbase,
                                          width=self.btn_width,
                                          command=self.click_managesubject)
        self.managesubject_button.pack(pady=10)

        self.exit_button = CTkButton(self.sidebar,
                                              text="Exit",
                                              font=("Bungee", 14),
                                              text_color=self.active_text,
                                              corner_radius=self.btn_cnr,
                                              fg_color=self.idle_color,
                                              hover_color=self.active_color,
                                              border_width=1,
                                              border_color=color_hhbase,
                                              width=self.btn_width,
                                              command=self.click_exit)
        self.exit_button.pack(pady=10)

    def click_dashboard(self):
        self.button_click_reset()
        self.active_frame = "DB"

        self.frame_class = DashboardFrame(self.mainframe)

        self.dashboard_button.configure(fg_color=self.active_color,
                                        hover_color=self.active_color,
                                        text_color=self.muted_text)

    def click_managetask(self):
        self.button_click_reset()
        self.active_frame = "MT"

        self.frame_class = ManageTasksFrame(self.mainframe)

        self.managetask_button.configure(fg_color=self.active_color,
                                         hover_color=self.active_color,
                                         text_color=self.muted_text)

    def click_managesubject(self):
        self.button_click_reset()
        self.active_frame = "MS"

        self.frame_class = ManageSubjectFrame(self.mainframe)

        self.managesubject_button.configure(fg_color=self.active_color,
                                            hover_color=self.active_color,
                                            text_color=self.muted_text)

    def click_exit(self):
        self.parent.destroy()

    def button_click_reset(self):
        self.dashboard_button.configure(fg_color=self.idle_color, hover_color=self.active_color, text_color=self.active_text)
        self.managetask_button.configure(fg_color=self.idle_color, hover_color=self.active_color, text_color=self.active_text)
        self.managesubject_button.configure(fg_color=self.idle_color, hover_color=self.active_color, text_color=self.active_text)

        hkasdh = TaskFileRead()
        hkasdh.save()

        if self.frame_class:
            self.frame_class.destroy_gui()