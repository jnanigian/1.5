import tkinter
from tkinter import *


master = Tk()

w = Canvas(master, width=200, height=100)
w=Canvas(master, background='green')
w.pack()
w.grid(row=0,column=1)
slider=Scale(master, from_=1, to =10, label="Speed",)
speed=slider
slider.grid(row=2, column=0)
w.create_rectangle(50, 25, 150, 75, fill="blue")


mainloop()
