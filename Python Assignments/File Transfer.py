#imports the libraries and widgets needed
import tkinter
from tkinter import filedialog
from tkinter import *
import shutil
import os
from os import *
from shutil import *

#creats the window
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        #defines the properties of the window
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('File Transfer')
        self.master.config(bg='lightgray')
        #creates the string variable to hold the text
        self.varText = StringVar()
        self.starting = StringVar()
        self.ending = StringVar()
        #defines what should go in the entry box
        #self.lblText = Label(self.master, text='', font=('Helvetica',16), fg='black', bg='lightgray')
        #self.lblText.grid(row=0, column=0,padx=(30,0),pady=(30,0))
        
        #self.txtText = Entry(self.master, text=self.varText, font=('Helvetica',16), fg='black', bg='lightblue')
        #self.txtText.grid(row=0, column=1,padx=(30,0),pady=(30,0))
        #the command to collect and publish the information to the webpage
        self.btnStart = Button(self.master, text="Starting Folder", width=20,height=2, command=self.Begin)
        self.btnStart.grid(row=2, column=0,padx=(10,0),pady=(30,0), sticky=NE)
        self.btnFinish = Button(self.master, text="Destitation Folder", width=20,height=2, command=self.End)
        self.btnFinish.grid(row=2, column=1,padx=(10,0),pady=(30,0), sticky=NE)
        self.btnTransfer = Button(self.master, text="Move Files", width=10,height=2, command=self.Move)
        self.btnTransfer.grid(row=2, column=2,padx=(10,0),pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10,height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=4,padx=(10,90),pady=(30,0), sticky=NE)

    def Begin(self):
        starting = filedialog.askdirectory()

    def End(self):
        ending = filedialog.askdirectory()

    def Move(self):
        source = self.starting.get()+"/"

        destination = self.ending.get()+"/"
        files = os.listdir(source)

        for i in files:
            shutil.move(source+i, destination)
                

    def cancel(self):
        self.master.destroy()
        
if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
        
