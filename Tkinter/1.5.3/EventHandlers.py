import Tkinter
master = Tkinter.Tk()

radius_intvar = Tkinter.IntVar()
radius_intvar.set(100)
x = 150
y = 150

def radius_changed(new_intval):

    r = radius_intvar.get()

    canvas.coords(circle_item, x-r, y-r, x+r, y+r)

radius_slider = Tkinter.Scale(master, from_=1, to=250, variable=radius_intvar,
                              label='Radius', command=radius_changed)
radius_slider.grid(row=1, column=0, sticky=Tkinter.W)

text = Tkinter.Label(master, text='Drag slider \n to adjust \n circle.')
text.grid(row=0, column=0)


canvas = Tkinter.Canvas(master, width=300, height=300, background='black')
canvas.grid(row=0, rowspan=2, column=1)


r = radius_intvar.get()
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r,
                                 outline='red', fill='red')

master.mainloop()
