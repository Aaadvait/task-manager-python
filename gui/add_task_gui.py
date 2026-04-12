from customtkinter import *
from gui.global_gui import *
from data.task_read import TaskFileRead

TYPE_OPTIONS = ["Assignment", "Study", "Project", "Practical", "Revision", "Exam", "Other"]
PAD = 18


class AddTaskSubFrame:
    def __init__(self, parent, upper_class):
        self.upper_class = upper_class
        self.app_state = TaskFileRead()
        self.app_state.refresh_subject_list()
        self.subject_list = self.app_state.sf["subject"].tolist()

        self.addtask_frame = CTkFrame(parent, fg_color=C_PAGE, corner_radius=0)
        self.addtask_frame.grid(row=0, column=0, sticky="nsew")
        self.addtask_frame.rowconfigure((0, 1), weight=0)
        self.addtask_frame.rowconfigure(2, weight=1)
        self.addtask_frame.columnconfigure(0, weight=1)

        self._build_topbar()
        self._build_form_panel()

    # ----- TOPBAR --------------------
    def _build_topbar(self):
        topbar_frame = CTkFrame(self.addtask_frame, fg_color="transparent")
        topbar_frame.grid(row=0, column=0, sticky="ew", padx=PAD, pady=(PAD, 8))
        topbar_frame.columnconfigure(0, weight=1)

        label_frame = CTkFrame(topbar_frame, fg_color='transparent')
        label_frame.grid(row=0, column=0, sticky= 'nsew')

        CTkFrame(label_frame, width=4, height=20, fg_color=C_TEAL).pack(side='left')
        CTkLabel(label_frame, text="  Add Task", font=F_HEAD,
                 text_color=C_TEXT).pack(side='left')

        CTkLabel(topbar_frame, text="--- Create a New Task ---",
                 font=F_SUB, text_color=C_MUTED).grid(row=1, column=0, sticky="w")

        icon_logo = CTkFrame(topbar_frame, fg_color="transparent",
                             width=36, height=36, corner_radius=18)
        icon_logo.grid(row=0, column=1, rowspan=2, sticky="e")

        CTkButton(icon_logo, text=" < ",
                  font=("Bungee", 12, "bold"),
                  fg_color=C_VIOLET_DIM,
                  border_color=C_VIOLET_BRD,
                  text_color=C_TEXT, width=32, height=32,
                  command=self.go_back).pack()

    # ----- MAIN --------------------
    def _build_form_panel(self):
        panel = CTkFrame(self.addtask_frame, fg_color=C_CARD,
                         corner_radius=14, border_width=1, border_color=C_BORDER)
        panel.grid(row=2, column=0, sticky="nsew", padx=PAD, pady=(0, PAD))
        panel.columnconfigure(0, weight=1)

        form = CTkFrame(panel, fg_color="transparent")
        form.grid(row=0, column=0, sticky="nsew", padx=16, pady=16)
        form.grid_columnconfigure((0, 1), weight=1)

        # Date
        CTkLabel(form, text="Enter Date: ", font=F_ATLF, text_color=C_TEXT2).grid(row=0, column=0, sticky="w")

        self.date_entry_grid = CTkFrame(form, height=32, fg_color="transparent")
        self.date_entry_grid.grid(row=1, column=0, sticky="ew", padx=(0, 8), pady=(4,12))
        self.date_entry_grid.columnconfigure((0,1,2), weight=0)
        self.date_entry_grid.columnconfigure(3, weight=1)
        self.date_entry_grid.rowconfigure(0, weight=1)

        self.date_day = CTkEntry(self.date_entry_grid, height=32, width=36,
                                 placeholder_text="DD", font=F_SUB,
                                 fg_color=C_VIOLET_DIM, border_color=C_VIOLET_BRD)
        self.date_day.grid(row=0, column=0, padx=(0,8))

        self.date_month = CTkEntry(self.date_entry_grid, height=32, width=36,
                                   placeholder_text="MM", font=F_SUB,
                                   fg_color=C_VIOLET_DIM, border_color=C_VIOLET_BRD)
        self.date_month.grid(row=0, column=1, padx=(0,8))

        self.date_year = CTkEntry(self.date_entry_grid, height=32, width=56,
                                  placeholder_text="YYYY", font=F_SUB,
                                  fg_color=C_VIOLET_DIM, border_color=C_VIOLET_BRD)
        self.date_year.grid(row=0, column=2 , padx=(0, 8))

        # Task No
        CTkLabel(form, text="Enter Task No:", font=F_ATLF, text_color=C_TEXT2)\
            .grid(row=0, column=1, sticky="w")
        self.taskno_entry = CTkEntry(form, height=32, fg_color=C_TEAL_DIM,
                                     text_color=C_TEXT, border_color=C_TEAL_BRD)
        self.taskno_entry.grid(row=1, column=1, sticky="ew", pady=(4, 12))

        # Subject
        CTkLabel(form, text="Select Subject", font=F_ATLF, text_color=C_TEXT2)\
            .grid(row=2, column=0, sticky="w")
        self.subject_dropdown = CTkOptionMenu(form, height=32,
                                              values=self.subject_list,
                                              fg_color=C_VIOLET_DIM,
                                              button_color=C_VIOLET,
                                              dropdown_fg_color=C_CARD2)
        self.subject_dropdown.grid(row=3, column=0, sticky="ew", padx=(0, 8), pady=(4, 12))

        # Type
        CTkLabel(form, text="Select Task Type", font=F_ATLF, text_color=C_TEXT2)\
            .grid(row=2, column=1, sticky="w")
        self.tasktype_dropdown = CTkOptionMenu(form, height=32,
                                               values=TYPE_OPTIONS,
                                               fg_color=C_VIOLET_DIM,
                                               button_color=C_VIOLET,
                                               dropdown_fg_color=C_CARD2)
        self.tasktype_dropdown.grid(row=3, column=1, sticky="ew", pady=(4, 12))

        # Priority
        CTkLabel(form, text="Select Priority", font=F_ATLF, text_color=C_TEXT2)\
            .grid(row=4, column=0, sticky="w")
        self.priority_option = CTkSegmentedButton(
            form, values=["High", "Normal"],
            selected_color=C_TEAL_HOV, unselected_color=C_TEAL_DIM
        )
        self.priority_option.set("Normal")
        self.priority_option.grid(row=5, column=0, sticky="ew", padx=(0, 8), pady=(4, 12))

        # Completion
        CTkLabel(form, text="Completion", font=F_ATLF, text_color=C_TEXT2).grid(row=4, column=1, sticky="w")
        self.completed_switch = CTkSwitch(form, text="Completed", progress_color=C_TEAL)
        self.completed_switch.grid(row=5, column=1, sticky="w", pady=(8, 12))

        # Description
        CTkLabel(form, text="Description", font=("DM Mono", 12), text_color=C_TEXT2).grid(row=6, column=0, sticky="w")

        self.description_box = CTkTextbox(form, height=150,
                                          fg_color=C_VIOLET_DIM,
                                          border_color=C_VIOLET_BRD,
                                          border_width=2)
        self.description_box.grid(row=7, column=0, columnspan=2,
                                  sticky="nsew", pady=(4, 12))

        # Buttons
        btn_row = CTkFrame(panel, fg_color="transparent")
        btn_row.grid(row=1, column=0, sticky="ew", padx=16, pady=(0, 16))
        btn_row.grid_columnconfigure((0, 1), weight=1)

        CTkButton(btn_row, text="Save Task", height=36,
                  fg_color=C_TEAL_DIM, text_color=C_TEAL,
                  command=self.save_task).grid(row=0, column=0, sticky="ew", padx=(0, 6))

        CTkButton(btn_row, text="Clear", height=36,
                  fg_color=C_ROSE_DIM, text_color=C_ROSE,
                  command=self.clear_form).grid(row=0, column=1, sticky="ew", padx=(6, 0))

    # ----- LOGIC --------------------

    def save_task(self):
        try:
            gday = int(self.date_day.get().strip())
            gmonth = int(self.date_month.get().strip())
            gyear = int(self.date_year.get().strip())

            taskno = int(self.taskno_entry.get())
            subject = self.subject_dropdown.get()
            tasktype = self.tasktype_dropdown.get()
            priority = 1 if self.priority_option.get() == "High" else 2
            completion = 1 if self.completed_switch.get() else 0
            desc = self.description_box.get("1.0", "end")

            if gday == "" or gday < 0 or gday > 31:
                raise Exception("Invalid Date - Day")
            if gmonth == "" or gmonth < 0 or gmonth > 12:
                raise Exception("Invalid Date - Month")
            if gyear == "":
                raise Exception("Invalid Date - Year")

            date = f"{gday}-{gmonth}-{gyear}"
            self.app_state.add_task(date, priority, completion,
                                    subject, tasktype, taskno, desc)

            self.clear_form()

        except Exception as e:
            print("ERROR:", e)

    def clear_form(self):
        self.date_day.delete(0, "end")
        self.date_month.delete(0, "end")
        self.date_year.delete(0, "end")
        self.taskno_entry.delete(0, "end")
        self.description_box.delete("1.0", "end")
        self.priority_option.set("Normal")
        self.completed_switch.deselect()

    def go_back(self):
        self.addtask_frame.destroy()
        self.upper_class.click_managetask()