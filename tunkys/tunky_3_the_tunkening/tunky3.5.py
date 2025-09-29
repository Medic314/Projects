from tkinter import Tk, Label

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

root = Tk()
label = Label(root, text="Drag Me!", bg="lightblue", width=10, height=2)
label.place(x=100,y=100)
label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)
root.mainloop()







from tkinter import *
window = Tk()
# Function to initialize the drag by capturing the initial mouse position
def drag_start(event):
    widget = event.widget  # Get the widget (label) that is being interacted with
    widget.startX = event.x  # Store the starting X position of the mouse within the widget
    widget.startY = event.y  # Store the starting Y position of the mouse within the widget

# Function to handle the motion of the mouse while dragging
def drag_motion(event):
    widget = event.widget  # Get the widget (label) that is being dragged
    # Calculate the new position by considering the current widget position and the mouse movement
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    # Move the widget to the new position using the `place` method
    widget.place(x=x, y=y)

# Create a red label with a specified size (width=10, height=5) and set its position to (0, 0)
label = Label(window, bg="red", width=10, height=5)
label.place(x=0, y=0)  # Position the label at coordinates (0, 0)

# Create a blue label with a specified size (width=10, height=5) and set its position to (100, 100)
label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=100, y=100)  # Position the label at coordinates (100, 100)

# Bind the left mouse button click event to start dragging (drag_start function) for the first label
label.bind("<Button-1>", drag_start)
# Bind the left mouse button motion event to move the label (drag_motion function) while dragging
label.bind("<B1-Motion>", drag_motion)

# Bind the left mouse button click event to start dragging (drag_start function) for the second label
label2.bind("<Button-1>", drag_start)
# Bind the left mouse button motion event to move the label (drag_motion function) while dragging
label2.bind("<B1-Motion>", drag_motion)

window.mainloop()