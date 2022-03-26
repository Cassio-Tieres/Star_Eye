import cam 
from tkinter import *

class Application:

    def __init__(self, master=None):

        self.title = Frame(master)
        self.title.pack()
        self.msg = Label(self.title, text = "Iniciar observações")
        self.msg.pack()

root = Tk()
Application(root)
root.mainloop()