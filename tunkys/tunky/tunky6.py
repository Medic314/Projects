import tkinter as tk

window = tk.Tk()
window.title("Scale Example")
window.geometry("400x300")

def get_value():
    value = scale.get()
    print(f"Selected value: {value}")

scale = tk.Scale(window, from_=0, to=100, orient="horizontal", length=400,
                 label="Selecct a Value", font=("Arial", 14), tickinterval=10)
scale.pack(pady=20)

button = tk.Button(window, text="Get Value", command=get_value)
button.pack()

window.mainloop()

from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ " degrees C")

window = Tk()

hotImage = PhotoImage(file='logo.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL, #orientation of scale
              font = ('Consolas',20),
              tickinterval = 10, #adds numeric indicators for value
              #showvalue = 0, #hide current value
              resolution = 5, #increment of slider
              troughcolor = '#69EAFF',
              fg = '#FF1C00',
              bg = '#111111'

              )
scale.set(((scale['from']-scale['to'])/2)+scale['to']) #set current value of slider

scale.pack()

coldImage = PhotoImage(file='logo.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()