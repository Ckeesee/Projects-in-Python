#imports the libraries and widgets needed
import webbrowser
import tkinter
from tkinter import *

#creats the window
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        #defines the properties of the window
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Text Generator for Personal Webpage')
        self.master.config(bg='lightgray')
        #creates the string variable to hold the text
        self.varText = StringVar()
        #defines what should go in the entry box
        self.lblText = Label(self.master, text='Enter the text for your webpage: ', font=('Helvetica',16), fg='black', bg='lightgray')
        self.lblText.grid(row=0, column=0,padx=(30,0),pady=(30,0))
        
        self.txtText = Entry(self.master, text=self.varText, font=('Helvetica',16), fg='black', bg='lightblue')
        self.txtText.grid(row=0, column=1,padx=(30,0),pady=(30,0))
        #the command to collect and publish the information to the webpage
        self.btnSubmit = Button(self.master, text="Submit", width=10,height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1,padx=(0,0),pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10,height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1,padx=(0,90),pady=(30,0), sticky=NE)

    def submit(self):
        webtext = self.varText.get()
        #creates and overwrites the webpage every time information is submited
        f = open('Personal_Web_Page.html', 'w')

        #generates the web page
        message = """
                <html>
                    <body>
                        <h1>
                            {}
                        </h1>
                    </body>
                </html>""".format(webtext)

        f.write(message)
        f.close()

        webbrowser.open_new_tab('Personal_Web_Page.html')
        self.master.destroy()

    def cancel(self):
        self.master.destroy()
        
if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
        
    
