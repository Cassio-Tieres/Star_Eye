from cgitb import text
from email.mime import image
from tkinter import font
from turtle import left, window_height, window_width
import cam 
import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title('Star Eye')

window_width = 1000
window_height = 630

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.resizable(False, False)

t_icon = tk.PhotoImage(file='assets/Icon.png')

title = ttk.Label(
    window,
    text='Star Eye',
    font=('Sail', 20),
    image=t_icon,
    compound=tk.RIGHT
).pack()


b_iniciarObservacao = ttk.Button(
    window,
    text='Iniciar observação',
    compound=tk.LEFT,
    
).pack(ipadx=20, ipady=10, expand=True)

window.mainloop()