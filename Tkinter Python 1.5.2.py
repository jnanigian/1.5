import Tkinter
from Tkinter import *


master = Tk()

w = Canvas(master, width=200, height=100)
w=Canvas(master, background='green')
w.pack()
w.grid(row=0,column=1)
speed = IntVar()
slider=Scale(master, from_=1, to =50, label="Speed", variable=speed)

slider.grid(row=2, column=0)
w.create_rectangle(50, 25, 150, 75, fill="blue")

w=speed.get()

box = Checkbutton(master, text="Check here.")
box.grid(row = 0, column = 0)

times_pressed = 0
def pressed():
    global times_pressed
    times_pressed = times_pressed + 1
    editor.insert(END, times_pressed)
    editor.see(END)
button = Button(master, text='Click me.', command=pressed)
button.grid(row = 1, column = 1)

editor = Text(width=30, height=4)
editor.grid(row = 2, column = 1, rowspan = 2, sticky = SE)

m=Label(master,text="By: Mason Ross & Jake Nanigian", bg = "green", fg = "red", font = ("Helvica", 17))


m.grid(row=0, column=1)

mainloop()
