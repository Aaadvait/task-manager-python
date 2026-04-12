from customtkinter import *

from data.task_read import TaskFileRead
from gui.global_gui import *


class ManageSubjectFrame:
    def __init__(self, parent, upper_class=None):
        self.upper_class = upper_class
        self.app_state = TaskFileRead()
        self.selected_subject = None
        self.subject_cards = []

        self.managesubject_frame = CTkFrame(parent, fg_color=C_PAGE, corner_radius=0)
        self.managesubject_frame.grid(row=0, column=0, sticky="nsew")
        self.managesubject_frame.grid_rowconfigure(1, weight=1)
        self.managesubject_frame.grid_columnconfigure(0, weight=1)

        self._build_header()
        self._build_editor_panel()
        self.refresh_view()

    def _build_header(self):
        header = CTkFrame(self.managesubject_frame, fg_color="transparent")
        header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=18, pady=(18, 12))
        header.grid_columnconfigure(0, weight=1)

        CTkLabel(header, text="Manage Subjects", font=F_TITLE, text_color=C_TEXT).grid(row=0, column=0, sticky="w")
        CTkLabel(header, text="Create subjects, rename them, or remove a subject and all of its tasks.", font=F_SUB, text_color=C_MUTED).grid(row=1, column=0, sticky="w", pady=(4, 0))

        self.view_subject_list = CTkButton(header,
                                           text="0 subjects", font=F_MONO_S, text_color=C_VIOLET,
                                           fg_color=C_VIOLET_DIM,
                                           corner_radius=12)
        self.view_subject_list.grid(row=0, column=1, rowspan=2, sticky="e")

    def _build_editor_panel(self):
        panel = CTkFrame(self.managesubject_frame, fg_color=C_CARD, corner_radius=14, border_width=1, border_color=C_BORDER)
        panel.grid(row=1, column=0, sticky="nsew", padx=(18, 9), pady=(0, 18))
        panel.grid_columnconfigure(0, weight=1)

        CTkLabel(panel, text="Subject Editor", font=F_LABEL, text_color=C_TEXT).grid(row=0, column=0, sticky="w", padx=16, pady=(16, 10))

        self.status_label = CTkLabel(panel, text="Add a new subject or select one from the right to rename it.", font=F_SUB, text_color=C_MUTED)
        self.status_label.grid(row=1, column=0, sticky="w", padx=16, pady=(0, 12))

        form = CTkFrame(panel, fg_color="transparent")
        form.grid(row=2, column=0, sticky="ew", padx=16)
        form.grid_columnconfigure(0, weight=1)

        CTkLabel(form, text="Subject Name", font=F_SUB, text_color=C_TEXT2).grid(row=0, column=0, sticky="w")
        self.subject_entry = CTkEntry(form, height=40)
        self.subject_entry.grid(row=1, column=0, sticky="ew", pady=(4, 16))

        button_row = CTkFrame(panel, fg_color="transparent")
        button_row.grid(row=4, column=0, sticky="ew", padx=16)
        button_row.grid_columnconfigure((0, 1), weight=1)

        CTkButton(button_row,
                  text="Add Subject", height=40, font=F_BTN,
                  fg_color=C_VIOLET, hover_color="#6C5CC8",
                  command=self.add_subject).grid(row=0, column=0, sticky="ew", padx=(0, 6))

        CTkButton(button_row,
                  text="Rename Selected", height=40, font=F_BTN,
                  fg_color=C_CARD2, hover_color=C_BORDER,
                  border_width=1, border_color=C_BORDER2,
                  command=self.rename_subject).grid(row=0, column=1, sticky="ew", padx=(6, 0))

        bottom_row = CTkFrame(panel, fg_color="transparent")
        bottom_row.grid(row=5, column=0, sticky="ew", padx=16, pady=(12, 16))
        bottom_row.grid_columnconfigure((0, 1), weight=1)

        CTkButton(bottom_row,
                  text="Delete Selected", height=36, font=F_BTN,
                  fg_color=C_ROSE_DIM, hover_color=C_ROSE, text_color=C_ROSE,
                  border_width=1, border_color=C_ROSE_BRD,
                  command=self.delete_subject).grid(row=0, column=0, sticky="ew", padx=(0, 6))

        CTkButton(bottom_row,
                  text="Clear Selection", height=36, font=F_BTN,
                  fg_color=C_TEAL_DIM, hover_color=C_TEAL, text_color=C_TEAL,
                  border_width=1, border_color=C_TEAL_BRD,
                  command=self.clear_form).grid(row=0, column=1, sticky="ew", padx=(6, 0))

    def refresh_view(self):
        self.app_state.refresh_dataframe()
        subjects = self.app_state.sf.tolist()
        self.header_badge.configure(text=f"{len(subjects)} subjects")



    def select_subject(self, subject):
        self.selected_subject = subject
        self.subject_entry.delete(0, "end")
        self.subject_entry.insert(0, subject)
        self.status_label.configure(text=f"Selected {subject}.", text_color=C_TEXT2)

    def add_subject(self):
        try:
            self.app_state.add_subject(self.subject_entry.get())
            self.status_label.configure(text="Subject added successfully.", text_color=C_TEAL)
            self.clear_form(reset_message=False)
            self.refresh_view()
        except Exception as exc:
            self.status_label.configure(text=str(exc), text_color=C_ROSE)

    def rename_subject(self):
        if not self.selected_subject:
            self.status_label.configure(text="Select a subject first.", text_color=C_ROSE)
            return
        try:
            self.app_state.rename_subject(self.selected_subject, self.subject_entry.get())
            self.status_label.configure(text="Subject renamed successfully.", text_color=C_TEAL)
            self.selected_subject = None
            self.clear_form(reset_message=False)
            self.refresh_view()
        except Exception as exc:
            self.status_label.configure(text=str(exc), text_color=C_ROSE)

    def delete_subject(self):
        if not self.selected_subject:
            self.status_label.configure(text="Select a subject first.", text_color=C_ROSE)
            return
        try:
            self.app_state.delete_subject(self.selected_subject)
            self.status_label.configure(text="Subject deleted successfully.", text_color=C_TEAL)
            self.selected_subject = None
            self.clear_form(reset_message=False)
            self.refresh_view()
        except Exception as exc:
            self.status_label.configure(text=str(exc), text_color=C_ROSE)

    def clear_form(self, reset_message=True):
        self.selected_subject = None
        self.subject_entry.delete(0, "end")
        if reset_message:
            self.status_label.configure(text="Add a new subject or select one from the right to rename it.", text_color=C_MUTED)

    def destroy_gui(self):
        self.managesubject_frame.destroy()
