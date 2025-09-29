from tkinter import Tk, Canvas, PhotoImage

def move_up(event):
    canvas.move(image, 0, -10)
def move_down(event):
    canvas.move(image, 0, 10)
def move_left(event):
    canvas.move(image, -10, 0)
def move_right(event):
    canvas.move(image, 10, 0)

root = Tk()
canvas = Canvas(root, width=400, height=400, bg="white")
canvas.pack()

photo = PhotoImage(file="logo.png")  # Use an image in your directory
image = canvas.create_image(200, 200, image=photo)

root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.mainloop()







#------------move widgets on window-------------
from tkinter import *

# Function to move the label (image) up by 10 pixels when the "w" key or Up arrow key is pressed
def move_up(event):
    # Get the current x and y positions of the label, and adjust the y position to move the label up by 10 pixels
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)

# Function to move the label (image) down by 10 pixels when the "s" key or Down arrow key is pressed
def move_down(event):
    # Get the current x and y positions of the label, and adjust the y position to move the label down by 10 pixels
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)

# Function to move the label (image) left by 10 pixels when the "a" key or Left arrow key is pressed
def move_left(event):
    # Get the current x and y positions of the label, and adjust the x position to move the label left by 10 pixels
    label.place(x=label.winfo_x()-10, y=label.winfo_y())

# Function to move the label (image) right by 10 pixels when the "d" key or Right arrow key is pressed
def move_right(event):
    # Get the current x and y positions of the label, and adjust the x position to move the label right by 10 pixels
    label.place(x=label.winfo_x()+10, y=label.winfo_y())

# Create the main window with a size of 500x500 pixels
window = Tk()
window.geometry("500x500")  # Set the window size to 500x500 pixels

# Bind key events to corresponding movement functions
# These keys allow the label to move in different directions
window.bind("<w>", move_up)  # Pressing "w" will move the label up
window.bind("<s>", move_down)  # Pressing "s" will move the label down
window.bind("<a>", move_left)  # Pressing "a" will move the label left
window.bind("<d>", move_right)  # Pressing "d" will move the label right
window.bind("<Up>", move_up)  # Pressing the Up arrow key will move the label up
window.bind("<Down>", move_down)  # Pressing the Down arrow key will move the label down
window.bind("<Left>", move_left)  # Pressing the Left arrow key will move the label left
window.bind("<Right>", move_right)  # Pressing the Right arrow key will move the label right

# Load the image file 'racecar.png' and create a Label widget to display it
myimage = PhotoImage(file='logo.png')  # Make sure the image file is in the same directory as the script
label = Label(window, image=myimage)  # Create a label with the image as its content
label.place(x=0, y=0)  # Place the label at the starting position (0, 0) 
window.mainloop()

#-------------move images on canvas-------------

from tkinter import *

# Function to move the image up by 10 pixels when the "w" key is pressed
def move_up(event):
    # Move the image 0 pixels horizontally (no change), and -10 pixels vertically (upward)
    canvas.move(myimage, 0, -10)

# Function to move the image down by 10 pixels when the "s" key is pressed
def move_down(event):
    # Move the image 0 pixels horizontally (no change), and 10 pixels vertically (downward)
    canvas.move(myimage, 0, 10)

# Function to move the image left by 10 pixels when the "a" key is pressed
def move_left(event):
    # Move the image -10 pixels horizontally (to the left), and 0 pixels vertically (no change)
    canvas.move(myimage, -10, 0)

# Function to move the image right by 10 pixels when the "d" key is pressed
def move_right(event):
    # Move the image 10 pixels horizontally (to the right), and 0 pixels vertically (no change)
    canvas.move(myimage, 10, 0)

# Create the main Tkinter window
window = Tk()

# Bind key events to corresponding movement functions
# These keys allow the image to move in different directions
window.bind("<w>", move_up)  # Pressing "w" will move the image up
window.bind("<s>", move_down)  # Pressing "s" will move the image down
window.bind("<a>", move_left)  # Pressing "a" will move the image left
window.bind("<d>", move_right)  # Pressing "d" will move the image right

# Create a canvas widget within the window, set its dimensions to 500x500 pixels
canvas = Canvas(window, width=500, height=500)
canvas.pack()  # Add the canvas to the window

# Load the image from the file 'racecar.png' to be used in the canvas
photoimage = PhotoImage(file='logo.png')  # Make sure the image file is available in the same directory
# Create an image on the canvas at coordinates (0, 0), with the image anchored to the top-left corner (NW)
myimage = canvas.create_image(0, 0, image=photoimage, anchor=NW)

window.mainloop()