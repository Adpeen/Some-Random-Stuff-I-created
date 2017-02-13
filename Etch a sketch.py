##Etch A Sketch
##05/15/15
##Adam Grierson

from tkinter import *##imports everything from tkinter 
canvas_height = 800##sets the canvas height
canvas_width = 600##sets the canvas width
canvas_color = "SlateGrey"##sets the canvas color
PenX = canvas_width/2
PenY = canvas_height/2
Pen_color = "Hot Pink"
line_width = 5
line_length = 5 

window = Tk()##Creates A window
window.title ("My Etch A Sketch")##gives a title to the window

canvas = Canvas(bg=canvas_color, height=canvas_height, width=canvas_width)
canvas.pack()##creates the canvas and packs everything together

def Up (event) :
    global PenY
    canvas.create_line(PenX, PenY, PenX, (PenY-line_length), width=line_width, fill=Pen_color)
    PenY = PenY - line_length

def Down (event) :
    global PenY
    canvas.create_line(PenX, PenY, PenX, (PenY-line_length), width=line_width, fill=Pen_color)
    PenY = PenY + line_length

def Right (event) :
    global PenX
    canvas.create_line(PenX, PenY, PenX+line_length, PenY ,width=line_width, fill=Pen_color)
    PenX= PenX + line_width

def Left (event) :
    global PenX
    canvas.create_line(PenX, PenY, PenX+line_length, PenY ,width=line_width, fill=Pen_color)
    PenX = PenX - line_width

def erase_all (event):
    global erase_all
    canvas.delete(ALL)

def Red (event):
    global Pen_color
    Pen_color = "Red"

def Blue(event):
    global Pen_color
    Pen_color = "Blue"

def Yellow(event):
    global Pen_color
    Pen_color = "Yellow"

def Green(event):
    global Pen_color
    Pen_color = "Green"
    
window.bind("<Up>",Up)
window.bind("<Down>",Down)
window.bind("<Right>",Right)
window.bind("<Left>",Left)
window.bind("e", erase_all)
window.bind("r", Red)
window.bind("b", Blue)
window.bind("y", Yellow)
window.bind("g", Green)
window.mainloop()
