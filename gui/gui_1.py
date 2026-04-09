from pathlib import Path

from Scripts.activate_this import abs_file
from customtkinter import *
from theme import *

#Getting the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent
RESOURCES = BASE_DIR / "resources"
icon_path = str(RESOURCES / "tm_icon.ico")
print(icon_path)

def disable_buttons():
    button_dashboard.configure(state="disabled")
    button_manage_task.configure(state="disabled")
    button_manage_subject.configure(state="disabled")
    button_exit.configure(state="disabled")

def enable_buttons():
    button_dashboard.configure(state="normal")
    button_manage_task.configure(state="normal")
    button_manage_subject.configure(state="normal")
    button_exit.configure(state="normal")

def view_loading(loading):

    disable_buttons()

    for child in main_section.winfo_children():
        child.grid_forget()

    loading.grid(row=0,column=0,sticky='nsew')

    loading_label = CTkLabel(loading,
                             text="-< Loading Task Manager, Please Wait... >-",
                             font=("Bungee", 20))
    loading_label.pack(expand=True)

    view_dashboard(dashboard_frame)
    enable_buttons()

def view_dashboard(dashboard):
    for child in main_section.winfo_children():
        child.grid_forget()

    dashboard.grid(row=0, column=0, sticky='nsew')
    dashboard.rowconfigure(0, weight=1)
    dashboard.rowconfigure(1, weight=1)
    dashboard.columnconfigure(0, weight=1)

    # IMPORTANT TASK FRAME
    imp_task_frame = CTkFrame(dashboard,
                              fg_color=color_hhbase,
                              corner_radius=0)
    imp_task_frame.grid(row=0, column=0, sticky='nsew')
    imp_task_frame_border_left = CTkFrame(imp_task_frame, fg_color=color_hbase, width=2)
    imp_task_frame_border_left.pack(fill="y", side="left")

    imp_task_label = CTkLabel(imp_task_frame,
                              text="❇️ Important Tasks",
                              font=("Bungee", 20))
    imp_task_label.pack()

    # UPCOMING TASK FRAME
    upc_task_frame = CTkFrame(dashboard,
                              fg_color=color_hhbase,
                              corner_radius=0)
    upc_task_frame.grid(row=1, column=0, sticky='nsew')
    upc_task_frame_border_left = CTkFrame(upc_task_frame, fg_color=color_hbase, width=2)
    upc_task_frame_border_left.pack(fill="y", side="left")
    upc_task_frame_border = CTkFrame(upc_task_frame, fg_color=color_hbase, height=2)
    upc_task_frame_border.pack(fill="x", side="top")

    upc_task_label = CTkLabel(upc_task_frame,
                              text="✳️ Upcoming Tasks",
                              font=("Bungee", 20))
    upc_task_label.pack()

def exit_prg(exit_f):

    disable_buttons()

    for child in main_section.winfo_children():
        child.grid_forget()

    exit_f.grid(row=0,column=0,sticky='nsew')

    loading_label = CTkLabel(exit_f,
                             text="-< Exiting the Task Manager >-",
                             font=("Bungee", 20))
    loading_label.pack(expand=True)

    #EXIT FUNCTION GOES HERE

    window.destroy()

#Making the window
window = CTk()
window.geometry("1280x720")
#window.resizable(False, False)
window.title("Task Manager")
window.iconbitmap(icon_path)
window.configure(fg_color=color_base)

#Configuring the MAIN space
window.rowconfigure(0, weight=1)    #Header
window.rowconfigure(1, weight=8)    #Main Body
window.rowconfigure(2, weight=1)    #Footer

window.columnconfigure(0, weight=1)

#Header         --------------------------------------------------
header_label = CTkLabel(window,
                        text='Task Manager',
                        font=('Bungee', 32))
header_label.grid(row=0, column=0)

#Body Frame     --------------------------------------------------
frame_main = CTkFrame(window,
                      fg_color=color_hbase,
                      corner_radius=0)
frame_main.grid(row=1,column=0,sticky='nsew')

frame_main.columnconfigure(0, weight=1) #Side Bar
frame_main.columnconfigure(1, weight=10) #Main Section

frame_main.rowconfigure(0, weight=1)

#SIDE BAR       --------------------------------------------------
sidebar = CTkFrame(frame_main,
                    fg_color=color_hhbase)
sidebar.grid(row=0,column=0,sticky='nsew')

sidebar.rowconfigure(0, weight=0)
sidebar.rowconfigure(1, weight=10)
sidebar.columnconfigure(0, weight=1)

#SIDE BAR TOP   --------------------------------------------------
sidebar_top = CTkFrame(sidebar,
                        fg_color=color_hhbase,
                        corner_radius=0)
sidebar_top.grid(row=0, column=0,
                  pady=0,
                  sticky='nsew')

sidebar_label1 = CTkLabel(sidebar_top,
                          text="⚙️ Controls",
                          font=("Bungee", 20))
sidebar_label1.pack(pady=10)

#SIDE BAR BOTTOM--------------------------------------------------

sidebar_bottom = CTkFrame(sidebar,
                           fg_color=color_hhbase,
                           corner_radius=0)
sidebar_bottom.grid(row=1, column=0,
                     pady=0,
                     sticky='nsew')

border_sidebar = CTkFrame(sidebar_bottom, height=2, fg_color=color_hbase)
border_sidebar.pack(fill="x", side="top")

button_dashboard = CTkButton(sidebar_bottom,
                             text="DashBoard",
                             font=("Bungee", 12),
                             fg_color=color_button)
button_dashboard.pack(pady=10)

button_manage_task = CTkButton(sidebar_bottom,
                               text="Manage Tasks",
                               font=("Bungee", 12),
                               fg_color=color_button)
button_manage_task.pack(pady=10)

button_manage_subject = CTkButton(sidebar_bottom,
                                  text="Manage Subjects",
                                  font=("Bungee", 12),
                                  fg_color=color_button)
button_manage_subject.pack(pady=10)

button_exit = CTkButton(sidebar_bottom,
                        text="EXIT",
                        font=("Bungee", 12),
                        fg_color=color_button)
button_exit.pack(pady=10)

label_sidebar_bottom = CTkLabel(sidebar_bottom,
                                text="-> Do It <-\nStay Consistent !",
                                font=("Bungee", 14))
label_sidebar_bottom.pack(pady=10, side="bottom")

#MAIN SECTION   --------------------------------------------------

main_section = CTkFrame(frame_main,
                     fg_color=color_hbase,
                     corner_radius=0)
main_section.grid(row=0, column=1, sticky='nsew')
main_section.rowconfigure(0, weight=1)
main_section.columnconfigure(0, weight=1)

dashboard_frame = CTkFrame(main_section)
manage_tasks_frame = CTkFrame(main_section)
manage_subjects_frame = CTkFrame(main_section)
loading_frame = CTkFrame(main_section)
exit_frame = CTkFrame(main_section)

button_dashboard.configure(command=lambda : view_dashboard(dashboard_frame))
button_exit.configure(command=lambda : exit_prg(exit_frame))

#Footer         --------------------------------------------------
footer_label = CTkLabel(window,
                        text="⚠️ OVER DUE TASKS",
                        font=("Bungee", 16),
                        text_color='#ce2d4f')
footer_label.grid(row=2,column=0,sticky='ew')

view_loading(loading_frame)
window.mainloop()