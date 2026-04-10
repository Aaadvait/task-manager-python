from global_gui import *
from customtkinter import *
from ui_body import BODY_FRAME

#Creating Main Window
window_main = CTk()
window_main.title("Task Manager")
window_main.iconbitmap(main_window_icon)
window_main.geometry("1280x720")
window_main.configure(fg_color=color_base)

#Configuring Window Grid
window_main.rowconfigure((0,2), weight=0)
window_main.rowconfigure(1, weight=1)       #Main Section
window_main.columnconfigure(0, weight=1)

BODY_FRAME(window_main)

window_main.mainloop()