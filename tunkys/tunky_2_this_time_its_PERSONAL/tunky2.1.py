from tkinter import Tk, Button
from tkinter.colorchooser import askcolor

def change_bg():
    color = askcolor()[1]
    if color:
        root.config(bg=color)

root = Tk()
root.geometry("300x300")
Button(root, text = "Choose Color", command=change_bg).pack()
root.mainloop()



"""from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(bg=colorHex)

window = Tk()
window.geometry("420x420")
button = Button(text='click me',command=click)
button.pack()
window.mainloop()"""