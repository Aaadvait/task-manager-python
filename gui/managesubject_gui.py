from customtkinter import *
from gui.global_gui import *
from data.task_read import TaskFileRead

PAD = 18


class ManageSubjectFrame:
    def __init__(self, parent, upper_class=None):
        self.upper_class = upper_class
        self.app_state = TaskFileRead()

        self.selected_subject = None
        self.subject_cards = []

        self.managesubject_frame = CTkFrame(parent, fg_color=C_PAGE, corner_radius=0)
        self.managesubject_frame.grid(row=0, column=0, sticky="nsew")

        self.managesubject_frame.columnconfigure((0, 1), weight=1)
        self.managesubject_frame.rowconfigure(1, weight=1)

        self._build_header()
        self._build_editor_panel()
        self._build_subject_panel()
        self.refresh_view()

    # ----- HEADER -------------------------

    def _build_header(self):
        header = CTkFrame(self.managesubject_frame, fg_color="transparent")
        header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=PAD, pady=(PAD, 12))
        header.columnconfigure(0, weight=1)

        CTkLabel(header, text="Manage Subjects", font=F_HEAD, text_color=C_TEXT).grid(row=0, column=0, sticky="w")

        CTkLabel(header,
                 text="Create subjects, rename subjects, remove subjects(w/tasks)",
                 font=F_SUB,
                 text_color=C_MUTED
        ).grid(row=1, column=0, sticky="w")

        self.view_subject_list = CTkLabel(
            header, text="0 subjects", font=F_MONO_S,
            fg_color=C_VIOLET_DIM, text_color=C_VIOLET, corner_radius=12
        )
        self.view_subject_list.grid(row=0, column=1, rowspan=2, sticky="e")

    # ----- LEFT PANEL -------------------------

    def _build_editor_panel(self):
        panel = CTkFrame(self.managesubject_frame, fg_color=C_CARD,
                         corner_radius=14, border_width=1, border_color=C_BORDER)
        panel.grid(row=1, column=0, sticky="nsew", padx=(PAD, 9), pady=(0, PAD))
        panel.columnconfigure(0, weight=1)

        label_frame = CTkFrame(panel, fg_color="transparent", height=36)
        label_frame.grid(row=0, column=0, sticky="ew", padx=16, pady=(16, 10))

        CTkFrame(label_frame, height=22, width=4, fg_color=C_VIOLET).pack(side="left")
        CTkLabel(label_frame, text="  Subject Editor", font=F_ATLF, text_color=C_TEXT).pack(side="left")

        self.status_label = CTkLabel(panel,
                                     text="Add or Select",
                                     font=F_SUB,
                                     text_color=C_MUTED,
        )
        self.status_label.grid(row=1, column=0, sticky="w", padx=16)

        self.subject_entry = CTkEntry(panel, height=40, fg_color=C_VIOLET_DIM, border_color=C_BORDER2)
        self.subject_entry.grid(row=2, column=0, sticky="ew", padx=16, pady=(6, 16))

        btn_frame = CTkFrame(panel, fg_color="transparent")
        btn_frame.grid(row=3, column=0, sticky="ew", padx=16)
        btn_frame.columnconfigure((0, 1), weight=1)

        CTkButton(btn_frame, text="Add Subject", fg_color=C_VIOLET,
                  command=self.add_subject).grid(row=0, column=0, sticky="ew", padx=(0, 6))

        CTkButton(btn_frame, text="Rename Selected",
                  fg_color=C_CARD2, border_width=1, border_color=C_BORDER2,
                  command=self.rename_subject).grid(row=0, column=1, sticky="ew", padx=(6, 0))

        bottom_row = CTkFrame(panel, fg_color="transparent")
        bottom_row.grid(row=4, column=0, sticky="ew", padx=16, pady=(12, 16))
        bottom_row.columnconfigure((0, 1), weight=1)

        CTkButton(bottom_row, text="Delete Selected",
                  fg_color=C_ROSE_DIM, text_color=C_ROSE,
                  command=self.delete_subject).grid(row=0, column=0, sticky="ew", padx=(0, 6))

        CTkButton(bottom_row, text="Clear Selection",
                  fg_color=C_TEAL_DIM, text_color=C_TEAL,
                  command=self.clear_form).grid(row=0, column=1, sticky="ew", padx=(6, 0))

    # ----- RIGHT PANEL -------------------------

    def _build_subject_panel(self):
        container = CTkFrame(self.managesubject_frame, fg_color=C_CARD,
                             corner_radius=14, border_width=1, border_color=C_BORDER)
        container.grid(row=1, column=1, sticky="nsew", padx=(9, PAD), pady=(0, PAD))
        container.columnconfigure(0, weight=1)
        container.rowconfigure(1, weight=1)

        self.subject_scroll = CTkScrollableFrame(container, fg_color="transparent",
                                                 scrollbar_fg_color="transparent", scrollbar_button_color=C_CARD2,
                                                 scrollbar_button_hover_color=C_VIOLET)
        self.subject_scroll.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))

        self.label_subject_list = CTkLabel(container, corner_radius=10, height=32,
                                           text="Subject List", text_color=C_TEXT2, font=F_ATLF,
                                           fg_color=C_VIOLET_DIM)
        self.label_subject_list.grid(row=0, column=0, sticky="ew", padx=16, pady=(8, 12))

    # ----- REFRESH VIEW -------------------------

    def refresh_view(self):
        self.app_state.refresh_dataframe()

        subjects = self.app_state.sf["subject"].tolist()
        tasks_df = self.app_state.df

        self.view_subject_list.configure(text=f"{len(subjects)} subjects")

        for card in self.subject_cards:
            card.destroy()
        self.subject_cards.clear()

        for subject in subjects:
            subject_tasks = tasks_df[tasks_df["subject"] == subject]

            total = len(subject_tasks)
            done = subject_tasks["completion"].sum()
            pending = total - done

            card = CTkFrame(self.subject_scroll, fg_color=C_CARD2, corner_radius=10)
            card.pack(fill="x", pady=6, padx=4)

            CTkLabel(card, text=subject, font=F_LABEL).pack(anchor="w", padx=12, pady=(6, 0))

            stats_row = CTkFrame(card, fg_color="transparent")
            stats_row.pack(anchor="w", padx=12, pady=(4, 8))

            CTkLabel(stats_row, text=f"Pending {pending}",
                     fg_color=C_ROSE_DIM, text_color=C_ROSE,
                     corner_radius=6, font=F_TAG).pack(side="left", padx=(0, 6))

            CTkLabel(stats_row, text=f"Done {int(done)}",
                     fg_color=C_TEAL_DIM, text_color=C_TEAL,
                     corner_radius=6, font=F_TAG).pack(side="left")

            CTkButton(card, text="Select", width=80,
                      fg_color=C_VIOLET_DIM,
                      border_color=C_BORDER2,
                      border_width=2,
                      text_color=C_TEXT2,
                      hover_color=C_VIOLET_BRD,
                      command=lambda s=subject: self.select_subject(s)
            ).pack(side="right", fill="y", padx=12, pady=(8,12))

            self.subject_cards.append(card)

    # ----- ACTIONS -------------------------

    def select_subject(self, subject):
        self.selected_subject = subject
        self.subject_entry.delete(0, "end")
        self.subject_entry.insert(0, subject)
        self.status_label.configure(text=f"Selected {subject}.", text_color=C_TEXT2)

    def add_subject(self):
        try:
            self.app_state.add_subject(self.subject_entry.get())
            self.refresh_view()
            self.clear_form(False)
        except Exception as exc:
            self.status_label.configure(text=str(exc), text_color=C_ROSE)

    def rename_subject(self):
        if not self.selected_subject: return
        self.app_state.rename_subject(self.selected_subject, self.subject_entry.get())
        self.selected_subject = None
        self.refresh_view()
        self.clear_form(False)

    def delete_subject(self):
        if not self.selected_subject: return
        self.app_state.delete_subject(self.selected_subject)
        self.selected_subject = None
        self.refresh_view()
        self.clear_form(False)

    def clear_form(self, reset_message=True):
        self.selected_subject = None
        self.subject_entry.delete(0, "end")
        if reset_message:
            self.status_label.configure(
                text="Add or Select",
                text_color=C_MUTED,
            )

    def destroy_gui(self):
        self.managesubject_frame.destroy()