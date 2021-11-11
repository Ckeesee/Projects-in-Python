from tkinter import*
from tkinter import messagebox
import tkinter as tk


import phonebook_gui
import phonebook_func


#Frame is the Tkinter frame class that our own class with inherit from
class ParentWindow(Frame):
    def __inti__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minsize(500,300) #(height, width)
        self.master.maxsize(500,300)
        #This center windwo method will center our app on the users screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0f0f0")
        #This protocol methos is a tkinter built-in method to catch if
        #the user clicks the upper corner, "X" on windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #load in the GUI widgets form a seperate module
        #keeping your code compartmetalized and cluster free
        phonebook_gui.load_gui(self)


if __name__=="__main__" :
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
