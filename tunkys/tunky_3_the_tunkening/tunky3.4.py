from tkinter import Tk, Label

def mouse_event(event):
    label.config(text=f"Mouse at ({event.x}, {event.y})")


root = Tk()
label = Label(root, text="Move your mouse!", font=("Arial", 16))
label.pack()
root.bind("<Motion>", mouse_event)
root.geometry("300x300")
root.mainloop()



from tkinter import *

def doSomething(event):
    print("Mouse coordinates: " + str(event.x)+","+str(event.y))

window = Tk()

window.bind("<Button-1>",doSomething) #left mouse click
window.bind("<Button-2>",doSomething) #scroll wheel
window.bind("<Button-3>",doSomething) #right mouse click
window.bind("<ButtonRelease>",doSomething)#mousebutton release
window.bind("<Enter>",doSomething) #enter the window
window.bind("<Leave>",doSomething) #leave the window
#window.bind("<Motion>",doSomething) #Where the mouse moved
window.mainloop()