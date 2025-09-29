import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = tk.Tk()
window.title("My Music Preferences")

label = Label(window, text="Welcome to My Music Preferences!", font=("Arial", 20), fg = "Purple")
label.pack(pady=20)

label = Label(window, text="Who is your favorite artist or band?", font=("Arial", 18))
label.pack()

entry = tk.Entry(window, font=("Arial", 16))
entry.pack(pady=10)

label = Label(window, text="Select your favorite music genres:", font=("Arial", 18))
label.pack()

rock = tk.IntVar()
pop = tk.IntVar()
jazz = tk.IntVar()

checkbox = tk.Checkbutton(window, text="Rock", variable=rock, font=("Arial", 16),).pack(anchor=W)
checkbox = tk.Checkbutton(window, text="Pop", variable=pop, font=("Arial", 16)).pack(anchor=W)
checkbox = tk.Checkbutton(window, text="Jazz", variable=jazz, font=("Arial", 16)).pack(anchor=W)




label = Label(window, text="Choose your preferred listening method:", font=("Arial", 18))
label.pack()

choice = tk.StringVar(value="")

tk.Radiobutton(window, text = "Streaming", variable = choice, value = "Streaming").pack(anchor="w")
tk.Radiobutton(window, text = "CDs", variable = choice, value = "CDs").pack(anchor="w")
tk.Radiobutton(window, text = "Vinyl", variable = choice, value = "Vinyl").pack(anchor="w")



def show_message():
    if rock.get() == 1:
       rock2 = "Rock, "
    if pop.get() == 1:
        pop2 = "Pop, "
    if jazz.get() == 1:
       jazz2 = "Jazz"

    user_input = entry.get()

    messagebox.showinfo(title='Music Preferences',message=f'Favorite Artist/Band: {user_input}\nFavorite Genres: {rock2}{pop2}{jazz2}\nPreferred Listening Method: {choice.get()}')

button = tk.Button(window, text="Submit", fg="White", bg="Blue", font=("Arial", 16), command=show_message)
button.pack()

window.mainloop()