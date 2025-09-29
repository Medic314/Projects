from tkinter import Tk, Text, Button


def print_text():
    content = text_area.get("1.0", "end-1c")
    print(content)

root = Tk()
text_area = Text(root, height=10, width=40, font=("Ink Free", 16))
text_area.pack()
Button(root, text="Submit", command = print_text).pack()
root.mainloop()



from tkinter import *
def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()
text = Text(window,
            bg="light yellow",
            font=("Ink Free",25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple")
text.pack()
button = Button(window,text="submit",command=submit)
button.pack()
window.mainloop()