from tkinter import *
from tkinter import Grid


def run():
    root = Tk()
    root.title("Tk Example")
    root.minsize(200, 200)  # width, height
    root.geometry("300x300+50+50")

    # Create Label in our window
    g = Grid()
    g.g

    image = PhotoImage(file="nedladdning.jpg")
    img = Label(root, image=image)
    img.pack()
    root.mainloop()

run()