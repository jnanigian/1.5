import Tkinter as tk

root = tk.Tk()
root.wm_title('Color-Shape Art Creation')

editor = tk.Text(root, width=10)
editor.grid(column=2, row=0, rowspan=3)

canvas = tk.Canvas(root, height=300, width=300, background='#FFFFFF')
canvas.grid(row=0, column=1, rowspan=3)

red_intvar = tk.IntVar()
green_intvar = tk.IntVar()
blue_intvar = tk.IntVar()

shapes = []

class ColorSlider(tk.Scale):


    def __init__(self, parent, myLabel, model_intvar, editor, canvas):

        def slider_changed(new_val):

            tk_color_string = color(red_intvar, green_intvar, blue_intvar)
            editor.insert(tk.END, tk_color_string + '\n')
            editor.see(tk.END)

            canvas.itemconfig(shapes[-1], fill=tk_color_string)

        tk.Scale.__init__(self, parent, orient=tk.HORIZONTAL, from_=0, to=255,
                               variable=model_intvar, label=myLabel, command=slider_changed)

red_slider = ColorSlider(root, 'Red:', red_intvar, editor, canvas)
red_slider.grid(row=1, column=0, sticky=tk.W)

green_slider = ColorSlider(root, 'Green:', green_intvar, editor, canvas)
green_slider.grid(row=2, column=0, sticky=tk.W)

blue_slider = ColorSlider(root, 'Blue:', blue_intvar, editor, canvas)
blue_slider.grid(row=3, column=0, sticky=tk.W)

message = tk.Label(root, text='Drag mouse to\ndraw circles.\nDrag sliders\nto change color.')
message.grid(column=0, row=0, sticky=tk.N)


for x in range(10, 300, 40):
    y = x
    r = 30
    new_circle = canvas.create_oval(x - r, y - r, x + r, y + r, outline='#000000')
    shapes.append(new_circle)
canvas.itemconfig(shapes[4], outline='green')

startx, starty = 300, 300



def down(event):
    global startx, starty
    startx = event.x
    starty = event.y


def up(event):
    tk_color_string = color(red_intvar, green_intvar, blue_intvar)
    r = (startx - event.x) ** 2 + (starty - event.y) ** 2
    r = int(r ** .5)
    new_shape = canvas.create_oval(startx - r, starty - r, startx + r, starty + r,
                                   fill=tk_color_string, outline='#000000')
    shapes.append(new_shape)

canvas.bind('<Button-1>', down)
canvas.bind('<ButtonRelease-1>', up)
def hexstring(slider_intvar):
    slider_int = slider_intvar.get()
    slider_hex = hex(slider_int)
    slider_hex_digits = slider_hex[2:]
    if len(slider_hex_digits) == 1:
        slider_hex_digits = '0' + slider_hex_digits
    return slider_hex_digits


def color(r, g, b):
    rx = hexstring(r)
    gx = hexstring(g)
    bx = hexstring(b)
    return '#' + rx + gx + bx
def write_slogan():
    length=len(shapes)-2
    print(length)
    print(shapes)
    canvas.itemconfig(shapes[length], outline='green', fill='#ff0000')


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Change last drawn objects color",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()

