from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Hello!")

frame = ttk.Frame(window)
frame.grid(column=0, row=0, sticky=(N, S, E, W))

label = ttk.Label(window, text = "Hello World!")
label.grid(column=0, row=0)

window.mainloop()