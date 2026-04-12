from customtkinter import *
from gui.global_gui import *
from data.task_read import TaskFileRead
from datetime import date

today = date.today()
f_today = today.strftime("%d-%m-%Y")

PAD = 18
GAP = 8

subject_list = ["ALL","Digi Elec", "AMT", "BIGASS_SUBJECT_NAME"]

class ManageTasksFrame:
    def __init__(self, parent):

        self.app_state = TaskFileRead()
        self.data_frame = self.app_state.df

        self.display_tasks = None
        self.get_display_tasks("ALL", "ALL")            #MANUAL CONTROL

        self.todays_tasks = self.app_state.get_today()
        self.overdue_tasks = self.app_state.get_overdue()

        self.task_rows = []

        self.managetask_frame = CTkFrame(parent,
                                         fg_color=C_PAGE,
                                         corner_radius=0)
        self.managetask_frame.grid(row=0, column=0, sticky='nsew')
        self.managetask_frame.rowconfigure((0, 1), weight=0)
        self.managetask_frame.rowconfigure(2, weight=1)
        self.managetask_frame.columnconfigure(0, weight=1)

        self._build_topbar()
        self._build_control_panel()
        self._build_task_panel()

    # --- Top Bar --------------------
    def _build_topbar(self):
        topbar_frame = CTkFrame(self.managetask_frame,
                                     fg_color="transparent")
        topbar_frame.grid(row=0, column=0, sticky="ew", padx=PAD, pady=(PAD, 8))
        topbar_frame.columnconfigure(0, weight=1)

        CTkLabel(topbar_frame, text="Task Manager", font=F_HEAD,
                 text_color=C_TEXT, anchor="w").grid(row=0, column=0, sticky="w")
        CTkLabel(topbar_frame, text=f"--- Manager for Tasks ---", font=F_SUB,
                 text_color=C_MUTED, anchor="w").grid(row=1, column=0, sticky="w")

        icon_logo = CTkFrame(topbar_frame, fg_color=C_VIOLET, width=36, height=36, corner_radius=18)
        icon_logo.grid(row=0, column=1, rowspan=2, sticky="e")
        CTkLabel(icon_logo, text="TM", font=("DM Sans", 14, "bold"),
                 text_color=C_TEXT, width=36, height=36).pack()

    # ----- Control Panel --------------------
    def _build_control_panel(self):
        row_f = CTkFrame(self.managetask_frame, fg_color="transparent")
        row_f.grid(row=1, column=0, sticky="ew", padx=PAD, pady=(0, 10))

        row_f.columnconfigure((0, 1, 2), weight=1)

        specs = [
            ("PRIORITY", ("ALL", "High", "Low"), C_ROSE, "> Sort by Priority"),
            ("SUBJECT", subject_list, C_VIOLET, "> Sort by subject"),
            ("ADD TASK", "ADD TASK", C_TEAL, "> Create a new Task"),
        ]

        for col, (lbl, btn_val, accent, sub) in enumerate(specs):
            pad_l = 0 if col == 0 else 6
            pad_r = 6 if col < 2 else 0

            tile = CTkFrame(row_f, fg_color=C_CARD, corner_radius=12,
                            border_width=1, border_color=C_BORDER,
                            width=200, height=110)  # <-- HARD LOCK SIZE
            tile.grid(row=0, column=col, padx=(pad_l, pad_r), sticky="nsew")
            tile.grid_propagate(False)

            # --- Accent top bar
            top_bar = CTkFrame(tile, fg_color=accent, height=2)
            top_bar.pack(fill="x")

            inner = CTkFrame(tile, fg_color="transparent")
            inner.pack(fill="both", expand=True, padx=14, pady=10)

            # --- Title
            CTkLabel(
                inner,
                text=lbl,
                font=("DM Mono", 10, "bold"),
                text_color=C_MUTED
            ).pack(anchor="w")

            # --- Main control
            if col == 2:
                CTkButton(
                    inner,
                    text=btn_val,
                    height=32,
                    font=("Bungee", 13),
                    fg_color=C_TEAL_DIM,
                    hover_color=C_TEAL_HOV,
                    text_color=C_TEAL,
                    border_width=1,
                    border_color=C_TEAL_BRD,
                    corner_radius=8
                ).pack(anchor="w", fill="x", pady=(6, 4))

            else:
                CTkOptionMenu(
                    inner,
                    values=btn_val,
                    width=160,  # <-- FIX WIDTH (KEY FIX)
                    height=32,
                    font=("Bungee", 13),
                    fg_color=C_CARD2,
                    button_color=accent,
                    button_hover_color=accent,
                    dropdown_fg_color=C_CARD2,
                    text_color=C_TEXT,
                    dynamic_resizing=False  # <-- CRITICAL
                ).pack(anchor="w", fill="x", pady=(6, 4))

            # --- Subtitle
            CTkLabel(
                inner,
                text=sub,
                font=F_MONO_S,
                text_color=accent
            ).pack(anchor="w")

    def _build_task_panel(self):
        panel = CTkFrame(self.managetask_frame, fg_color=C_CARD,
                         corner_radius=14, border_width=1, border_color=C_BORDER)
        panel.grid(row=2, column=0, sticky="nsew", padx=PAD, pady=(0, PAD))
        panel.rowconfigure(2, weight=1)
        panel.columnconfigure(0, weight=1)
        self.panel = panel

        hdr = CTkFrame(panel, fg_color="transparent")
        hdr.grid(row=0, column=0, sticky="ew", padx=16, pady=(14, 10))
        hdr.columnconfigure(0, weight=1)

        left = CTkFrame(hdr, fg_color="transparent")
        left.grid(row=0, column=0, sticky="w")
        CTkFrame(left, fg_color=C_VIOLET, width=4, height=20).grid(row=0, column=0)
        CTkLabel(left, text="  To Do :-",
                 font=("DM Sans", 13, "bold"),
                 text_color=C_TEXT).grid(row=0, column=1)

        self.count_badge = CTkLabel(
            hdr,
            text=f"  {len(self.display_tasks)} tasks  ",
            font=("DM Mono", 11, "bold"),
            fg_color=C_VIOLET_DIM,
            text_color="#9B8FE8",
            corner_radius=10
        )
        self.count_badge.grid(row=0, column=1, sticky="e")

        CTkFrame(panel, fg_color=C_BORDER, height=1).grid(
            row=1, column=0, sticky="ew", padx=16, pady=(0, 6)
        )

        self.tasklist_frame = CTkScrollableFrame(
            panel, fg_color="transparent",
            scrollbar_button_color=C_CARD2,
            scrollbar_button_hover_color=C_VIOLET
        )
        self.tasklist_frame.grid(row=2, column=0, sticky="nsew",
                                 padx=10, pady=(0, 10))
        self.tasklist_frame.columnconfigure(0, weight=1)

        self.build_task_list()

    def build_task_list(self):
        for i, row in enumerate(self.display_tasks.itertuples()):
            action = lambda x=row: self.on_click(x)

            rf = CTkFrame(self.tasklist_frame, fg_color=C_CARD2,
                          corner_radius=10, border_width=1, border_color=C_BORDER)
            rf.grid(row=i, column=0, sticky="ew", padx=4, pady=GAP // 2)
            rf.columnconfigure(1, weight=1)

            # color logic
            dot_color = C_VIOLET
            if row.Index in self.todays_tasks.index:
                dot_color = C_ROSE
            if row.Index in self.overdue_tasks.index:
                dot_color = C_ROSE

            dot = CTkFrame(rf, fg_color=dot_color, width=8, height=8, corner_radius=4)
            dot.grid(row=0, column=0, padx=(14, 0))

            txt = CTkFrame(rf, fg_color="transparent")
            txt.grid(row=0, column=1, sticky="w", padx=10, pady=10)

            subj_btn = CTkButton(txt, text=row.subject,
                                 font=("DM Sans", 12, "bold"),
                                 fg_color="transparent", hover_color=C_CARD,
                                 text_color=C_TEXT2, anchor="w", height=20,
                                 #command=lambda idx=i: self.complete_task(idx)
                                 )
            subj_btn.pack(anchor="w")

            tag_row = CTkFrame(txt, fg_color="transparent")
            tag_row.pack(anchor="w", pady=(4, 0))
            CTkLabel(tag_row, text=f" {row.tasktype} ", font=F_TAG,
                     fg_color=C_VIOLET_DIM, text_color="#9B8FE8",
                     corner_radius=5).pack(side="left", padx=(0, 4))
            CTkLabel(tag_row, text=f" #{row.taskno} ", font=F_TAG,
                     fg_color=C_CARD, text_color=C_MUTED,
                     corner_radius=5).pack(side="left")

            af = CTkFrame(rf, fg_color="transparent")
            af.grid(row=0, column=2, sticky="e", padx=(0, 12))

            cbtn = CTkButton(af, text="Complete",
                             width=96, height=28, font=F_BTN,
                             fg_color=C_TEAL_DIM, hover_color=C_TEAL_HOV,
                             text_color=C_TEAL, border_width=1,
                             border_color=C_TEAL_BRD, corner_radius=8,
                             #command=lambda idx=i: self.complete_task(idx)
                             )
            cbtn.pack(side="left", padx=(0, 6))

            CTkButton(af, text="Remove",
                      width=86, height=28, font=F_BTN,
                      fg_color=C_ROSE_DIM, hover_color=C_ROSE_HOV,
                      text_color=C_ROSE, border_width=1,
                      border_color=C_ROSE_BRD, corner_radius=8,
                      #command=lambda idx=i: self.confirmation_window(idx)
                      ).pack(side="left")

            self.task_rows.append({
                "frame": rf,
                "main_btn": subj_btn,
                "dot": dot,
                "data": row,
                "cbtn": cbtn,
                "cbtn_st": 0,
            })

    # ----- Click Control -------------------------

    def on_click(selfx, x):
        pass

    def destroy_gui(self):
        self.managetask_frame.destroy()

    # ----- Data Control -------------------------

    def get_display_tasks(self, subject="ALL", priority="ALL"):

        if subject == "ALL" and priority == "ALL":
            self.display_tasks = self.app_state.df[self.app_state.df["completion"] == 0
                                                    ].sort_values(by=["date", "priority"], ascending=[True, True])
        elif subject == "ALL" and priority != "ALL":
            self.display_tasks = self.app_state.df[((self.app_state.df["priority"] == priority) &
                                                   (self.app_state.df["completion"] == 0))
                                                    ].sort_values(by=["date", "priority"], ascending=[True, True])
        elif subject != "ALL" and priority == "ALL":
            self.display_tasks = self.app_state.df[(self.app_state.df["subject"] == subject) &
                                                   (self.app_state.df["completion"] == 0)
                                                    ].sort_values(by=["date", "priority"], ascending=[True, True])
        else:
            self.display_tasks = self.app_state.df[(self.app_state.df["priority"] == priority) &
                                                   (self.display_tasks["subject"] == subject)&
                                                   (self.app_state.df["completion"] == 0)
                                                    ].sort_values(by=["date", "priority"], ascending=[True, True])

        for row in self.display_tasks:
            print(row)