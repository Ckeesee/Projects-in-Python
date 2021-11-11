import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3

import Student_Tracking_gui
import Student_Tracking_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(700,400) #(Height, Width)
        self.master.maxsize(700,400)
        # This CenterWindow method will center our app on the user's screen
        Student_Tracking_func.center_window(self,700,400)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: Student_Tracking_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        Student_Tracking_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
