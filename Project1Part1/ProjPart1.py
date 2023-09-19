from tkinter import *

#Create an instance of tkinter frame with size set
root = Tk()
root.geometry("600x600")
root.title("Canvas")

#Two functions defined to get intial click point coordinates and corresponding points during mouse drag
#to create a line that join all these points. As a line is made of various points, distance between them is negligible.
#This forms a free shape as drawn on canvas.

# Method to get initial click point coordinates during mouse drag
def get_xy(event):
    #declared global as to use in other function
    global last_x, last_y
    last_x, last_y = event.x, event.y

# Method to create line
def draw(event):
    global last_x, last_y
    # Canvas method with starting points as previous captured point coordinates and new point coordinates are mouse click
    #event point coordinates
    canvas.create_line((last_x, last_y, event.x, event.y), fill='red', width=5)
    #Need to update coordinates as start point changes during mouse drag
    last_x, last_y = event.x, event.y

# Method to clear canvas
def clear(event):
    canvas.delete('all')

# Create a canvas
canvas = Canvas(root, bg='black')
canvas.pack(anchor="nw", fill="both", expand=1)

#Bind methods to call respective functions based on event

#Mouse left click calls method to capture intial point
canvas.bind("<Button-1>", get_xy)
#Left mouse button being held down calls method to draw line
canvas.bind("<B1-Motion>", draw)
#Mouse right click calls method to clear canvas
canvas.bind("<Button-2>", clear)

root.mainloop()
