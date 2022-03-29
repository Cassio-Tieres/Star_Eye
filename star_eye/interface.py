from cgitb import text
from email.mime import image
from tkinter import font
from turtle import left
import cam 
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('1000x653')
window.resizable(False, False)

t_icon = tk.PhotoImage(file='assets/Icon.png')

title = ttk.Label(
    window,
    text='Star Eye',
    font=('Sail', 20),
    image=t_icon,
    compound=tk.LEFT
).pack()


b_iniciarObservacao = ttk.Button(
    window,
    text='Iniciar observação',
    width=30,
    compound=tk.LEFT,
    
).pack()

window.mainloop()