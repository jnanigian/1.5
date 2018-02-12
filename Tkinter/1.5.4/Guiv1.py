from tkinter import *
import tkinter
"""paint.py: not exactly a paint program.. just a smooth line drawing demo."""

b1 = "up"
xold, yold = None, None
color = 'black'



def main():
    root = Tk()

    def canvasd():
        Canvas.delete("all")



    def buttonPressed(which):
        if which == 'list':
            global color
            print
            'List selected ', listbox.get(listbox.curselection())
            color = listbox.get(listbox.curselection())

    # canvas creation
    drawing_area = Canvas(root)
    drawing_area.pack()

    # binding
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)

    # list box creation
    listbox = Listbox(root)
    for item in ['red', 'green', 'blue','orange', 'yellow', 'black','purple','white','pink']:
        listbox.insert(END, item)
    listbox.pack()

    Button(root, text="List Select", command=lambda: buttonPressed('list')).pack()


    root.mainloop()


def b1down(event):
    global b1
    b1 = "down"  # you only want to draw when the button is down
    # because "Motion" events happen -all the time-


def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None  # reset the line when you let go of the button
    yold = None


def motion(event):
    if b1 == "down":
        global xold, yold, color
        if xold is not None and yold is not None:
            event.widget.create_line(xold, yold, event.x, event.y, fill=color, smooth=TRUE)
            # here's where you draw it. smooth. neat.
        xold = event.x
        yold = event.y


if __name__ == "__main__":
    main()
