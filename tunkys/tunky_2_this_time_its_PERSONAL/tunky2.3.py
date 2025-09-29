from tkinter import Tk, Button
from tkinter.filedialog import askopenfilename

def open_file():
    file_path = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            print(file.read())

root = Tk()
Button(root, text="Open File", command=open_file).pack()
root.mainloop()



from tkinter import Tk, Text, Button
from tkinter.filedialog import asksaveasfilename

def save_file():
    file_path = asksaveasfilename(defaultextension=".txt",
                                   filetypes=[("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get("1.0", "end-1c"))

root = Tk()
text_area = Text(root)
text_area.pack()
Button(root, text="Save File", command=save_file).pack()
root.mainloop()