from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        # create a new root widget using Tk() and save it as a data member
        self.root = Tk()
        # Set the title property of the root widget
        self.root.title("Maze Solver")
        # Create a Canvas widget and save it as a data member.
        self.canvas = Canvas(self.root, bg="white", width=width, height=height)
        # Pack the canvas widget so that it's ready to be drawn
        self.canvas.pack(fill=BOTH, expand=1)
        # Create a data member to represent that the window is "running", and set it to False
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    # Method to call the root widget's update_idletasks() and update() methods. Each time this is called, the window will redraw itself
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    #  Method to set the data member we created to track the "running" state of the window to True. Next, it should call self.redraw() over and over as long as the running state remains True.
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    # Method to close the window
    def close(self):
        self.running = False

    # Draw line method
    #  Takes an instance of a Line and a fill color as input, then calls the Line's draw method
    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)


# Class Point
# Stores 2 public data members
# x - the x-coordinate (horizontal) in pixels of the point
# y - the y-coordinate (vertical) in pixels of the point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Class Line
#  takes 2 points as input, and save them as data members
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # Method draw
    # takes a canvas as input
    # draws a line on the canvas from the start point to the end point
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )
