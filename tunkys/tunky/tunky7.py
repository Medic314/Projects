import tkinter as tk

window = tk.Tk()
window.title("Listbox Example")
window.geometry("400x300")

def show_selection():
    selected_item = listbox.get(tk.ACTIVE)
    print(f"Selected item: {selected_item}")

def add_item():
    new_item = entry.get()
    if new_item:
        listbox.insert(tk.END, new_item)

def delete_item():
    listbox.delete(tk.END)

listbox = tk.Listbox(window, font=("Arial", 14), width = 25, height = 8)
listbox.pack(pady=10)

listbox.insert(1, "Apple")
listbox.insert(2, "Banana")
listbox.insert(3, "Cherry")

entry = tk.Entry(window, font=("Arial", 14))
entry.pack()

add_button = tk.Button(window, text="Add Item", command=add_item)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Item", command=delete_item)
delete_button.pack(pady=5)

show_button = tk.Button(window, text="Show Selection", command=show_selection)
show_button.pack(pady=5)

window.mainloop()

# listbox = A listing of selectable text items within it's own container

def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())

from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia",35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

frame = Frame(window)
frame.pack()

submitButton = Button(frame,text="submit",command=submit)
submitButton.pack(side=LEFT)

addButton = Button(frame,text="add",command=add)
addButton.pack(side=LEFT)

deleteButton = Button(frame,text="delete",command=delete)
deleteButton.pack(side=LEFT)

window.mainloop()
