from turtle import left
import cam 
from tkinter import *

class Application:

    def __init__(self, master=None):

        self.title = Frame(master)
        self.title.pack()
        self.msg = Label(self.title, text = "Star Eye")
        self.msg["font"] = ("Arsenal", "20", "bold")
        self.msg.pack(side=LEFT)

        self.iniciarObs = Button(self.title)
        self.iniciarObs["text"] = "iniciar Observações"
        self.iniciarObs["font"] = ("Arsenal", "15")
        self.iniciarObs["width"] = 20
        self.iniciarObs["height"] = 2
        self.iniciarObs.bind("<Button-1>", self.openCam)
        self.iniciarObs.pack(side=RIGHT)

    def openCam(self, event):
        cam.captacaoVideo()

root = Tk()
Application(root)
root.mainloop()