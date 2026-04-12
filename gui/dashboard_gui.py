from customtkinter import *
from gui.global_gui import *
from data.task_read import TaskFileRead
from datetime import date
import pandas as pd

today = date.today()
f_today = today.strftime("%d-%m-%Y")

PAD = 18
GAP = 8

class DashboardFrame:
    def __init__(self, parent, upper_class):
        self.window_popup  = None
        self.task_button   = None
        self.app_state     = TaskFileRead()
        self.data_frame    = self.app_state.df
        self.upper_class   = upper_class

        # --- DATA ---
        self.high_priority = self.app_state.get_high_priority()
        self.today_tasks   = self.app_state.get_today()
        self.over_due_tasks = self.app_state.get_overdue()

        self.display_tasks = (
            pd.concat([self.high_priority, self.today_tasks, self.over_due_tasks])
            .drop_duplicates().sort_values(by=["date", "priority"], ascending=[True, True])
        )

        self.task_rows = []

        # --- UI ---
        self.dashboard_frame = CTkFrame(parent, fg_color=C_PAGE, corner_radius=0)
        self.dashboard_frame.grid(row=0, column=0, sticky="nsew")
        self.dashboard_frame.rowconfigure(0, weight=0)
        self.dashboard_frame.rowconfigure(1, weight=0)
        self.dashboard_frame.rowconfigure(2, weight=1)
        self.dashboard_frame.columnconfigure(0, weight=1)

        self._build_topbar()
        self._build_stats()
        self._build_task_panel()

    # ----- Top Bar --------------------
    def _build_topbar(self):
        bar = CTkFrame(self.dashboard_frame, fg_color="transparent")
        bar.grid(row=0, column=0, sticky="ew", padx=PAD, pady=(PAD, 8))
        bar.columnconfigure(0, weight=1)

        CTkLabel(bar, text="Task Dashboard", font=F_HEAD,
                 text_color=C_TEXT, anchor="w").grid(row=0, column=0, sticky="w")
        CTkLabel(bar, text=f"Today: {f_today}", font=F_SUB,
                 text_color=C_MUTED, anchor="w").grid(row=1, column=0, sticky="w")

        icon_logo = CTkFrame(bar, fg_color=C_VIOLET, width=36, height=36, corner_radius=18)
        icon_logo.grid(row=0, column=1, rowspan=2, sticky="e")
        CTkLabel(icon_logo, text="TM", font=("DM Sans", 14, "bold"),
                 text_color=C_TEXT, width=36, height=36).pack()

    # ----- Stats --------------------
    def _build_stats(self):
        row_f = CTkFrame(self.dashboard_frame, fg_color="transparent")
        row_f.grid(row=1, column=0, sticky="ew", padx=PAD, pady=(0, 10))
        row_f.columnconfigure((0, 1, 2), weight=1)

        total = len(self.app_state.df[self.app_state.df["completion"] == 0])
        high  = len(self.high_priority)
        done  = int(self.app_state.df["completion"].sum()) \
                if "completion" in self.app_state.df.columns else 0

        specs = [
            ("TOTAL",    str(total), C_VIOLET, "tasks"),
            ("PRIORITY", str(high),  C_ROSE,   "need attention"),
            ("DONE",     str(done),  C_TEAL,   "completed"),
        ]

        for col, (lbl, val, accent, sub) in enumerate(specs):
            pad_l = 0 if col == 0 else 6
            pad_r = 6 if col < 2 else 0

            tile = CTkFrame(row_f, fg_color=C_CARD, corner_radius=12,
                            border_width=1, border_color=C_BORDER)
            tile.grid(row=0, column=col, padx=(pad_l, pad_r), sticky="nsew")

            top_bar = CTkFrame(tile, fg_color=accent, height=2)
            top_bar.pack(fill="x")

            inner = CTkFrame(tile, fg_color="transparent")
            inner.pack(fill="both", expand=True, padx=14, pady=10)

            title_label = CTkLabel(inner, text=lbl, font=("DM Mono", 10, "bold"),
                                   text_color=C_MUTED)
            title_label.pack(anchor="w")

            value_label = CTkLabel(inner, text=val, font=("DM Mono", 28, "bold"),
                                   text_color=accent)
            value_label.pack(anchor="w")

            sub_label = CTkLabel(inner, text=sub, font=F_MONO_S,
                                 text_color=accent)
            sub_label.pack(anchor="w")

            if lbl == "TOTAL":
                tile.bind("<Button-1>", lambda e: self.upper_class.click_managetask())
                inner.bind("<Button-1>", lambda e: self.upper_class.click_managetask())
                title_label.bind("<Button-1>", lambda e: self.upper_class.click_managetask())
                value_label.bind("<Button-1>", lambda e: self.upper_class.click_managetask())
                sub_label.bind("<Button-1>", lambda e: self.upper_class.click_managetask())
                top_bar.bind("<Button-1>", lambda e: self.upper_class.click_managetask())

    # --- Task Panel ------------------------
    def _build_task_panel(self):
        panel = CTkFrame(self.dashboard_frame, fg_color=C_CARD,
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
        CTkLabel(left, text="  High Priority Tasks",
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

    # --- Task List ---------------
    def build_task_list(self):
        if len(self.display_tasks) > 0:
            for i, row in enumerate(self.display_tasks.itertuples()):
                action = lambda x=row: self.on_click(x)

                rf = CTkFrame(self.tasklist_frame, fg_color=C_CARD2,
                              corner_radius=10, border_width=1, border_color=C_BORDER)
                rf.grid(row=i, column=0, sticky="ew", padx=4, pady=GAP // 2)
                rf.columnconfigure(1, weight=1)

                # color logic
                dot_color = "#FF0000"
                if row.Index in self.today_tasks.index:
                    dot_color = C_VIOLET
                if row.Index in self.high_priority.index:
                    dot_color = C_ROSE
                if row.Index in self.high_priority.index and row.Index in self.today_tasks.index:
                    dot_color = C_RED
                if row.Index in self.over_due_tasks.index:
                    dot_color = C_BORDER

                dot = CTkFrame(rf, fg_color=dot_color, width=8, height=8, corner_radius=4)
                dot.grid(row=0, column=0, padx=(14, 0))

                txt = CTkFrame(rf, fg_color="transparent")
                txt.grid(row=0, column=1, sticky="w", padx=10, pady=10)

                subj_btn = CTkButton(txt, text=row.subject,
                                     font=("DM Sans", 12, "bold"),
                                     fg_color="transparent", hover_color=C_CARD,
                                     text_color=C_TEXT2, anchor="w", height=20,
                                     command=action)
                subj_btn.pack(anchor="w")

                tag_row = CTkFrame(txt, fg_color="transparent")
                tag_row.pack(anchor="w", pady=(4, 0))
                CTkLabel(tag_row, text=f" {row.tasktype} -{row.taskno}", font=F_TAG,
                         fg_color=C_VIOLET_DIM, text_color="#9B8FE8",
                         corner_radius=5).pack(side="left", padx=(0, 4))
                CTkLabel(tag_row, text=f" Due: {row.date} ", font=F_TAG,
                         fg_color=C_CARD, text_color=C_MUTED,
                         corner_radius=5).pack(side="left")

                af = CTkFrame(rf, fg_color="transparent")
                af.grid(row=0, column=2, sticky="e", padx=(0, 12))

                cbtn = CTkButton(af, text="Complete",
                                 width=96, height=28, font=F_BTN,
                                 fg_color=C_TEAL_DIM, hover_color=C_TEAL_HOV,
                                 text_color=C_TEAL, border_width=1,
                                 border_color=C_TEAL_BRD, corner_radius=8,
                                 command=lambda idx=i: self.complete_task(idx))
                cbtn.pack(side="left", padx=(0, 6))

                CTkButton(af, text="Remove",
                          width=86, height=28, font=F_BTN,
                          fg_color=C_ROSE_DIM, hover_color=C_ROSE_HOV,
                          text_color=C_ROSE, border_width=1,
                          border_color=C_ROSE_BRD, corner_radius=8,
                          command=lambda idx=i: self.confirmation_window(idx)
                          ).pack(side="left")

                self.task_rows.append({
                    "frame": rf,
                    "main_btn": subj_btn,
                    "dot": dot,
                    "data": row,
                    "cbtn": cbtn,
                    "cbtn_st": 0,
                    "dot_colour": dot_color
                })
        else:
            rf = CTkFrame(self.tasklist_frame, fg_color=C_ROSE_DIM,
                          corner_radius=100, border_width=1, border_color=C_BORDER)
            rf.grid(row=0, column=0, sticky="ew", padx=4, pady=GAP // 2)
            rf.columnconfigure(1, weight=1)

            nothing_label = CTkLabel(rf,
                                     text="No tasks to show here",
                                     fg_color="transparent",
                                     text_color=C_ROSE,
                                     font=("Bungee", 16)
                                     )
            nothing_label.grid(column=1, row=0, sticky='nsew')

            self.task_rows.append({
                "frame": rf,
            })

    # --- Button Click Functions ---------------

    def on_click(self, x):
        popup = CTkToplevel(self.dashboard_frame, fg_color=C_PAGE)
        popup.geometry("420x320")
        popup.title("Task Details")
        popup.resizable(False, False)
        popup.grab_set()

        # Center popup
        popup.update_idletasks()
        px, py = popup.master.winfo_rootx(), popup.master.winfo_rooty()
        pw, ph = popup.master.winfo_width(), popup.master.winfo_height()
        popup.geometry(f"420x320+{px + pw // 2 - 210}+{py + ph // 2 - 160}")

        # --- Card ---
        card = CTkFrame(popup, fg_color=C_CARD, corner_radius=14,
                        border_width=1, border_color=C_BORDER)
        card.pack(fill="both", expand=True, padx=14, pady=14)

        # --- Title ---
        CTkLabel(card,
                 text=f"{x.subject}",
                 font=F_HEAD,
                 text_color=C_TEXT).pack(anchor="w", padx=16, pady=(12, 4))

        # --- Info row ---
        info = CTkFrame(card, fg_color="transparent")
        info.pack(anchor="w", padx=16, pady=(0, 10))

        CTkLabel(info,
                 text=f"{x.tasktype} - {x.taskno}",
                 font=F_TAG,
                 fg_color=C_VIOLET_DIM,
                 text_color=C_VIOLET,
                 corner_radius=6).pack(side="left", padx=(0, 6))

        CTkLabel(info,
                 text=f"Due: {x.date}",
                 font=F_TAG,
                 fg_color=C_CARD2,
                 text_color=C_TEXT2,
                 corner_radius=6).pack(side="left")

        # --- Meta ---
        meta = CTkFrame(card, fg_color="transparent")
        meta.pack(anchor="w", padx=16, pady=(0, 10))

        priority_text = "High" if x.priority == 1 else "Low"
        completion_text = "Completed" if x.completion == 1 else "Pending"

        CTkLabel(meta,
                 text=f"Priority: {priority_text}",
                 font=F_BODY,
                 text_color=C_TEXT).pack(anchor="w")

        CTkLabel(meta,
                 text=f"Status: {completion_text}",
                 font=F_BODY,
                 text_color=C_TEXT).pack(anchor="w")

        # --- Description ---
        CTkLabel(card,
                 text="Description:",
                 font=F_LABEL,
                 text_color=C_TEXT).pack(anchor="w", padx=16, pady=(6, 2))

        desc_box = CTkTextbox(card,
                              height=100,
                              fg_color=C_CARD2,
                              text_color=C_TEXT,
                              border_width=1,
                              border_color=C_BORDER)
        desc_box.pack(fill="both", expand=False, padx=16, pady=(0, 12))

        desc_box.insert("1.0", x.taskdisc)
        desc_box.configure(state="disabled")

        # --- Close Button ---
        CTkButton(card,
                  text="Close",
                  height=32,
                  font=F_BTN,
                  fg_color=C_VIOLET_DIM,
                  hover_color=C_VIOLET_BRD,
                  text_color=C_VIOLET,
                  border_width=1,
                  border_color=C_VIOLET_BRD,
                  corner_radius=8,
                  command=popup.destroy).pack(pady=(0, 12))

    def complete_task(self, idx):
        item = self.task_rows[idx]
        row  = item["data"]

        if item["cbtn_st"] == 0:
            self.app_state.df.loc[
                (self.app_state.df["subject"] == row.subject) &
                (self.app_state.df["tasktype"] == row.tasktype) &
                (self.app_state.df["taskno"] == row.taskno),
                "completion"
            ] = 1
            item["main_btn"].configure(text_color=C_MUTED)
            item["dot"].configure(fg_color=C_TEAL)
            item["cbtn"].configure(text="Completed", fg_color=C_TEAL,
                                   text_color="#0B0D17", border_color=C_TEAL)
            item["cbtn_st"] = 1
        else:
            self.app_state.df.loc[
                (self.app_state.df["subject"] == row.subject) &
                (self.app_state.df["tasktype"] == row.tasktype) &
                (self.app_state.df["taskno"] == row.taskno),
                "completion"
            ] = 0
            item["main_btn"].configure(text_color=C_TEXT2)
            item["dot"].configure(fg_color=item["dot_colour"])
            item["cbtn"].configure(text="Complete", fg_color=C_TEAL_DIM,
                                   text_color=C_TEAL, border_color=C_TEAL_BRD)
            item["cbtn_st"] = 0

        self.app_state.save()

        self.app_state.refresh_dataframe()
        self.high_priority = self.app_state.get_high_priority()
        self.today_tasks = self.app_state.get_today()
        self.over_due_tasks = self.app_state.get_overdue()

        self.display_tasks = (
            pd.concat([self.high_priority, self.today_tasks, self.over_due_tasks])
            .drop_duplicates().sort_values(by=["date", "priority"], ascending=[True, True])
        )

    def remove_task(self, idx):
        self.window_popup.destroy()
        item = self.task_rows[idx]
        row = item["data"]

        self.app_state.df = self.app_state.df[~(
                (self.app_state.df["subject"] == row.subject) &
                (self.app_state.df["tasktype"] == row.tasktype) &
                (self.app_state.df["taskno"] == row.taskno)
        )].reset_index(drop=True)

        self.app_state.save()

        for t in self.task_rows:
            t["frame"].destroy()
        self.task_rows.clear()

        self.app_state.refresh_dataframe()
        self.high_priority = self.app_state.get_high_priority()
        self.today_tasks = self.app_state.get_today()
        self.over_due_tasks = self.app_state.get_overdue()

        self.display_tasks = (
            pd.concat([self.high_priority, self.today_tasks, self.over_due_tasks])
            .drop_duplicates().sort_values(by=["date", "priority"], ascending=[True, True])
        )

        self.build_task_list()

        self.count_badge.configure(text=f"  {len(self.high_priority)} tasks  ")

    def confirmation_window(self, idx):
        popup = CTkToplevel(self.dashboard_frame, fg_color=C_PAGE)
        popup.geometry("320x170")
        popup.grab_set()
        popup.title("Confirm Removal")
        popup.resizable(False, False)
        self.window_popup = popup

        popup.update_idletasks()
        px, py = popup.master.winfo_rootx(), popup.master.winfo_rooty()
        pw, ph = popup.master.winfo_width(), popup.master.winfo_height()
        popup.geometry(f"320x170+{px + pw // 2 - 160}+{py + ph // 2 - 85}")

        card = CTkFrame(popup, fg_color=C_CARD, corner_radius=14,
                        border_width=1, border_color="#2D1F40")
        card.pack(fill="both", expand=True, padx=12, pady=12)

        top = CTkFrame(card, fg_color="transparent")
        top.pack(fill="x", padx=18, pady=(16, 12))

        icon_bg = CTkFrame(top, fg_color=C_ROSE_DIM, width=36, height=36,
                           corner_radius=8, border_width=1, border_color=C_ROSE_BRD)
        icon_bg.pack(side="left")
        CTkLabel(icon_bg, text="<!>", font=("DM Sans", 18, "bold"),
                 text_color=C_ROSE, width=36, height=36).pack()

        txt = CTkFrame(top, fg_color="transparent")
        txt.pack(side="left", padx=12)
        CTkLabel(txt, text="Remove this task?",
                 font=("DM Sans", 13, "bold"), text_color=C_TEXT,
                 anchor="w").pack(anchor="w")
        CTkLabel(txt, text="This action cannot be undone.",
                 font=F_SUB, text_color=C_MUTED, anchor="w").pack(anchor="w")

        brow = CTkFrame(card, fg_color="transparent")
        brow.pack(pady=(0, 14))
        CTkButton(brow, text="Yes, Remove", width=120, height=32,
                  font=("DM Sans", 12, "bold"),
                  fg_color=C_ROSE, hover_color="#B8405E",
                  text_color="#fff", corner_radius=8,
                  command=lambda: self.remove_task(idx)).pack(side="left", padx=(0, 8))
        CTkButton(brow, text="Cancel", width=100, height=32,
                  font=("DM Sans", 12, "bold"),
                  fg_color=C_CARD2, hover_color=C_BORDER,
                  text_color="#9B8FE8", border_width=1, border_color=C_BORDER2,
                  corner_radius=8, command=popup.destroy).pack(side="left")

    def destroy_gui(self):
        self.dashboard_frame.destroy()