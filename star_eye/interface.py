from cgitb import text
from email.mime import image
from re import X
from textwrap import fill
from tkinter import font
from turtle import left, window_height, window_width
import cam 
import tkinter as tk
from tkinter import ttk

def abrirCamera():
    cam.captacaoVideo()

window = tk.Tk()

window.title('Star Eye')
window.iconbitmap('assets/Icon.ico')

window_width = 1000
window_height = 450

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.resizable(False, False)

t_icon = tk.PhotoImage(file='assets/Icon.png')

title = tk.Label(
    window,
    text='Star Eye',
    font=('Asar', 20),
    image=t_icon,
    compound=tk.RIGHT
).pack()

separator = ttk.Separator(window, orient='horizontal').pack(fill='x')

b_iniciarObservacao = ttk.Button(
    window,
    text='Iniciar observação',
    compound=tk.LEFT,
    command=abrirCamera
).pack(ipadx=20, ipady=10, expand=True)




window.mainloop()