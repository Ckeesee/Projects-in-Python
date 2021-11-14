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
        #defines what should go in the entry box
        #self.lblText = Label(self.master, text='', font=('Helvetica',16), fg='black', bg='lightgray')
        #self.lblText.grid(row=0, column=0,padx=(30,0),pady=(30,0))
        
        #self.txtText = Entry(self.master, text=self.varText, font=('Helvetica',16), fg='black', bg='lightblue')
        #self.txtText.grid(row=0, column=1,padx=(30,0),pady=(30,0))
        #the command to collect and publish the information to the webpage

        self.btnTransfer = Button(self.master, text="Move Files", width=10,height=2, command=self.Move)
        self.btnTransfer.grid(row=2, column=2,padx=(10,0),pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10,height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=4,padx=(10,90),pady=(30,0), sticky=NE)

    def Move(self):
        source = filedialog.askdirectory()+"/"
        files = os.listdir(source)
        if len(files)==0:
            self.lblText = Label(self.master, text='No files found in this location select again! {}'.format(os.path.basename(os.path.normpath(source))), font=('Helvetica',16), fg='black', bg='lightgray')
            self.lblText.grid(row=3, column=1,padx=(30,0),pady=(30,0))
            source = filedialog.askdirectory()+"/"
        else:
            self.lblText = Label(self.master, text='Transfering file from: {}'.format(os.path.basename(os.path.normpath(source))), font=('Helvetica',16), fg='black', bg='lightgray')
            self.lblText.grid(row=3, column=1,padx=(30,0),pady=(30,0))
        
        
        destination = filedialog.askdirectory()+"/"

        self.lblText = Label(self.master, text='Transfering file to: {}'.format(os.path.basename(os.path.normpath(destination))), font=('Helvetica',16), fg='black', bg='lightgray')
        self.lblText.grid(row=4, column=1,padx=(30,0),pady=(30,0))
        
        files = os.listdir(source)

        for i in files:
            shutil.move(source+i, destination)

    
        self.lblText = Label(self.master, text='File transfer Complete!', font=('Helvetica',16), fg='black', bg='lightgray')
        self.lblText.grid(row=5, column=1,padx=(30,0),pady=(30,0))
        
                    

    def cancel(self):
        self.master.destroy()
        
if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
        
