from idlelib.configdialog import font_sample_text

from customtkinter import *

from gui.global_gui import *
from data.task_read import TaskFileRead


class DashboardFrame:
    def __init__(self, parent):

        self.window_popup = None

        self.pad_value = 20
        self.row_spacing = 8

        self.app_state = TaskFileRead()
        self.data_frame = self.app_state.df
        self.high_priority = self.app_state.get_high_priority()
        self.all_tasks = self.app_state.get_all_pending()    #for all the non importaint tasks whichh will be displayed top top box 

        # --- Main Frame ---
        self.dashboard_frame = CTkFrame(
            parent,
            fg_color=color_mainframe,
            corner_radius=0
        )
        self.dashboard_frame.grid(row=0, column=0, sticky='nsew')
        self.dashboard_frame.rowconfigure(0, weight=1)
        self.dashboard_frame.rowconfigure(1, weight=20)
        self.dashboard_frame.columnconfigure(0, weight=1)

        # --- Summary Frame ---
        self.summary_frame = CTkFrame(
            self.dashboard_frame,
            fg_color=color_5a,
            corner_radius=10
        )
        self.summary_frame.grid(
            row=0, column=0,
            sticky='nsew',
            padx=self.pad_value,
            pady=self.pad_value
        )

        # --- Below Summary Frame ---
        self.below_summary_frame = CTkFrame(self.dashboard_frame, fg_color=color_5a)
        self.below_summary_frame.grid(row=1,column=0,sticky='nsew',padx=self.pad_value,pady=self.pad_value)
        self.below_summary_frame.columnconfigure(0, weight=1)
        self.below_summary_frame.rowconfigure(0, weight=0)
        self.below_summary_frame.rowconfigure(1, weight=1)

        # --- Important Tasks Label ---
        self.imptask_label = CTkLabel(
            self.below_summary_frame,
            text= "_ Important Tasks _",
            font=("Bungee", 16),
        )
        self.imptask_label.grid(row=0,column=0,sticky='nsew')


        # --- Task List Frame ---
        self.tasklist_frame = CTkScrollableFrame(
            self.below_summary_frame,
            fg_color="transparent",
            scrollbar_button_color=color_5a,
            scrollbar_button_hover_color=color_5
        )
        self.tasklist_frame.grid(
            row=1, column=0,
            sticky='nsew',
        )
        self.tasklist_frame.columnconfigure(0, weight=1)

        self.task_rows = []
        self.build_task_list()
        self.build_all_task_list()  #this ive added for all tasks to be visible 

    # -----------------------------
    def build_all_task_list(self):   #played around for a bit but ig backend is good to go UI needs fix
        for i, row in enumerate(self.all_tasks.itertuples()):
            text = f"{row.subject} {row.tasktype} No.{row.taskno}"

            lbl = CTkLabel(
            self.alltask_frame,
            text=text,
            anchor="w",
            font=("Bungee", 12)
            )
            lbl.pack(fill="x", padx=10, pady=5)
    #------------------------------------
    def build_task_list(self):
        for i, row in enumerate(self.high_priority.itertuples()):
            button_string = f"-> {row.subject} {row.tasktype} No.{row.taskno}"
            action = lambda x=button_string: self.on_click(x)

            row_frame = CTkFrame(
                self.tasklist_frame,
                corner_radius=8,
                fg_color=color_5
            )
            row_frame.grid(
                row=i,
                column=0,
                sticky="ew",
                padx=10,
                pady=self.row_spacing
            )
            row_frame.columnconfigure(0, weight=4)
            row_frame.columnconfigure(1, weight=1)

            btn = CTkButton(
                row_frame,
                text=button_string,
                height=36,
                anchor='w',
                font=("Bungee", 12),
                fg_color="transparent",
                hover_color=color_5b,
                text_color="white",
                command=action
            )
            btn.grid(row=0, column=0, sticky="ew", padx=10, pady=6)

            actions_frame = CTkFrame(row_frame, fg_color="transparent")
            actions_frame.grid(row=0, column=1, sticky="e", padx=10)

            complete_btn = CTkButton(
                actions_frame,
                text="Complete",
                width=36,
                height=28,
                font=("Bungee", 12),
                fg_color=color_6a,
                hover_color=color_6,
                command=lambda idx=i: self.complete_task(idx)
            )
            complete_btn.pack(side="left", padx=(0, 5))

            remove_btn = CTkButton(
                actions_frame,
                text="Remove",
                width=36,
                height=28,
                font=("Bungee", 12),
                fg_color=color_6a,
                hover_color=color_6,
                command=lambda idx=i: self.confirmation_window(idx)
            )
            remove_btn.pack(side="left")

            task_item = {
                "frame": row_frame,
                "main_btn": btn,
                "data": row,
                "cbtn": complete_btn,
                "cbtn_st": 0
            }
            self.task_rows.append(task_item)

    # -----------------------------

    def on_click(self, x):
        pass

    # -----------------------------

    def complete_task(self, idx):
        item = self.task_rows[idx]
        row = item["data"]

        if item["cbtn_st"] == 0:
            self.app_state.df.loc[
                self.app_state.df["taskno"] == row.taskno, "completion"
            ] = 1

            item["main_btn"].configure(text_color=color_3)
            item["cbtn"].configure(text="Completed")
            item["cbtn_st"] = 1

        else:
            self.app_state.df.loc[
                self.app_state.df["taskno"] == row.taskno, "completion"
            ] = 0

            item["main_btn"].configure(text_color=color_4)
            item["cbtn"].configure(text="Complete")
            item["cbtn_st"] = 0

        self.app_state.save()

    # -----------------------------

    def remove_task(self, idx):

        self.window_popup.destroy()

        item = self.task_rows[idx]
        row = item["data"]

        self.app_state.df = self.app_state.df[
            self.app_state.df["taskno"] != row.taskno
        ]

        self.app_state.save()

        # Refresh UI
        for item in self.task_rows:
            item["frame"].destroy()

        self.task_rows.clear()
        self.high_priority = self.app_state.get_high_priority()
        self.build_task_list()

    # -----------------------------

    def confirmation_window(self, idx):
        self.window_popup = CTkToplevel(self.dashboard_frame, fg_color=color_base)
        self.window_popup.geometry("300x150")
        self.window_popup.grab_set()
        self.window_popup.title("NOTICE!")
        self.window_popup.iconbitmap(delete_cross_icon)

        self.window_popup.update_idletasks()

        width = 300
        height = 150

        parent_x = self.window_popup.master.winfo_rootx()
        parent_y = self.window_popup.master.winfo_rooty()
        parent_width = self.window_popup.master.winfo_width()
        parent_height = self.window_popup.master.winfo_height()

        x = parent_x + (parent_width // 2) - (width // 2)
        y = parent_y + (parent_height // 2) - (height // 2)
        self.window_popup.geometry(f"{width}x{height}+{x}+{y}")

        label = CTkLabel(
            self.window_popup,
            text="Remove task?",
            font=("Arial", 16)
        )
        label.pack(pady=(25, 15))

        btn_frame = CTkFrame(self.window_popup, fg_color="transparent")
        btn_frame.pack(pady=10)

        yes_btn = CTkButton(
            btn_frame,
            text="Yes",
            width=100,
            command=lambda: self.remove_task(idx),
        )
        yes_btn.pack(side="left", padx=10)

        no_btn = CTkButton(
            btn_frame,
            text="No",
            width=100,
            command=self.window_popup.destroy
        )
        no_btn.pack(side="left", padx=10)

    # -----------------------------

    def destroy_gui(self):
        self.dashboard_frame.destroy()
