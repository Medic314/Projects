import tkinter as tk

window =tk.Tk()
window.title("Radio Button Example")
window.geometry("400x300")

choice = tk.IntVar(value=0)

tk.Radiobutton(window, text = "Option 1", variable = choice, value = 1).pack(anchor="w")
tk.Radiobutton(window, text = "Option 2", variable = choice, value = 2).pack(anchor="w")
tk.Radiobutton(window, text = "Option 3", variable = choice, value = 3).pack(anchor="w")

def show_choice():
    print(f"Selected option: {choice.get()}")

button = tk.Button(window, text="Submit", command=show_choice)
button.pack()

window.mainloop()



# radio button = similar to checkbox, but you can only select one from a group
from tkinter import *

food = ["pizza","hamburger","hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza!")
    elif(x.get()==1):
        print("You ordered a hamburger!")
    elif(x.get()==2):
        print("You ordered a hotdog!")
    else:
        print("huh?")

window = Tk()

pizzaImage = PhotoImage(file='logo.png')
hamburgerImage = PhotoImage(file='logo.png')
hotdogImage = PhotoImage(file='logo.png')
foodImages = [pizzaImage,hamburgerImage,hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], #adds text to radio buttons
                              variable=x, #groups radiobuttons together if they share the same variable
                              value=index, #assigns each radiobutton a different value
                              padx = 25, #adds padding on x-axis
                              font=("Impact",50),
                              image = foodImages[index], #adds image to radiobutton
                              compound = 'left', #adds image & text (left-side)
                              #indicatoron=0, #eliminate circle indicators
                              #width = 375, #sets width of radio buttons
                              command=order #set command of radiobutton to function
                              )
    radiobutton.pack(anchor=W)
window.mainloop()