import Tkinter

master = Tkinter.Tk()
master.wm_title('Hexadecimal Explorer')

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
                                 outline='black', fill='black')
red_intvar = Tkinter.IntVar()
red_intvar.set(100)
green_intvar = Tkinter.IntVar()
green_intvar.set(100)


def color_changed(new_intval):

    editor.insert(Tkinter.END, '#' + \
                           hexstring(red_intvar) + \
                           hexstring(green_intvar) + '00\n')
    editor.see(Tkinter.END)

    circle_item = canvas.create_oval(20,20,120,120,
                                     outline = '#222222', fill = "#" + \
                                     hexstring(red_intvar) + \
                                     hexstring(green_intvar) + "22")

red_slider = Tkinter.Scale(master, from_=0, to=255, variable=red_intvar,
                           orient=Tkinter.HORIZONTAL,
                           label='Red', command=color_changed)
red_slider.grid(row=5, column=0, sticky=Tkinter.E)
green_slider = Tkinter.Scale(master, from_=0, to=255, variable=green_intvar,
                             orient=Tkinter.HORIZONTAL,
                             label='Green', command=color_changed)
green_slider.grid(row=2, column=0, sticky=Tkinter.E)

text = Tkinter.Label(master, text='Drag slider \n to adjust \n color code. ')
text.grid(row=0, column =0)


editor = Tkinter.Text(master, width=10)
editor.grid(column=76, row=0, rowspan=3)



def hexstring(slider_intvar):


    slider_int = slider_intvar.get()

    slider_hex = hex(slider_int)

    slider_hex_digits = slider_hex[2:]

    if len(slider_hex_digits)==1:
        slider_hex_digits = '0' + slider_hex_digits
    return slider_hex_digits


master.mainloop()
