from tkinter import *
window = Tk()
window.geometry("475x500")
tile_image = PhotoImage(file="tests/tile_smallish.png")
select_image = PhotoImage(file="tests/select_small.png")

canvas = Canvas(window, width=475, height=500, bg="white")
canvas.pack()

if True:
    tile = canvas.create_image(100, 50, image=tile_image, anchor=NW)
    tile2 = canvas.create_image(100, 186, image=tile_image, anchor=NW)
    tile3 = canvas.create_image(100, 118, image=tile_image, anchor=NW)
    tile4 = canvas.create_image(100, 254, image=tile_image, anchor=NW)
    tile5 = canvas.create_image(100, 322, image=tile_image, anchor=NW)
    tile6 = canvas.create_image(100, 390, image=tile_image, anchor=NW)

    tile7 = canvas.create_image(168, 50, image=tile_image, anchor=NW)
    tile8 = canvas.create_image(168, 186, image=tile_image, anchor=NW)
    tile9 = canvas.create_image(168, 118, image=tile_image, anchor=NW)
    tile10 = canvas.create_image(168, 254, image=tile_image, anchor=NW)
    tile11 = canvas.create_image(168, 322, image=tile_image, anchor=NW)
    tile12 = canvas.create_image(168, 390, image=tile_image, anchor=NW)

    tile13 = canvas.create_image(236, 50, image=tile_image, anchor=NW)
    tile14 = canvas.create_image(236, 186, image=tile_image, anchor=NW)
    tile15 = canvas.create_image(236, 118, image=tile_image, anchor=NW)
    tile16 = canvas.create_image(236, 254, image=tile_image, anchor=NW)
    tile17 = canvas.create_image(236, 322, image=tile_image, anchor=NW)
    tile18 = canvas.create_image(236, 390, image=tile_image, anchor=NW)

    tile19 = canvas.create_image(304, 50, image=tile_image, anchor=NW)
    tile20 = canvas.create_image(304, 186, image=tile_image, anchor=NW)
    tile21 = canvas.create_image(304, 118, image=tile_image, anchor=NW)
    tile22 = canvas.create_image(304, 254, image=tile_image, anchor=NW)
    tile23 = canvas.create_image(304, 322, image=tile_image, anchor=NW)
    tile24 = canvas.create_image(304, 390, image=tile_image, anchor=NW)

def move_up(event):
    canvas.move(select, 0, -68)
def move_down(event):
    canvas.move(select, 0, 68)
def move_left(event):
    canvas.move(select, -68, 0)
def move_right(event):
    canvas.move(select, 68, 0)

window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)


select = canvas.create_image(100, 50, image=select_image, anchor=NW)

window.mainloop()