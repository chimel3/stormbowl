import tkinter as tk
import math

class Pitch(tk.Frame):
    def __init__(self, master, parms):
        self.rows = parms[0]
        self.columns = parms[1]
        self.size = parms[2]
        tk.Frame.__init__(self, master, borderwidth=10, bg="green")
        
        # Set the window size. Change this to be more dynamic depending on hex size
        classes.game.Game.set_window_size(master, "700x700")
        
    def create_canvas(self):
        hex_height = self.size * 2
        hex_width = math.sqrt(3)/2 * hex_height
        self.canvas = tk.Canvas(self,
                                borderwidth=0,
                                highlightthickness=0,
                                width=(self.columns * hex_width + (hex_width / 2)), 
                                height=(self.rows * (hex_height * 0.75)) + (hex_height * 0.25),
                                background="blue")
        self.canvas.pack()
        
        # need to return the canvas since this is a function rather than the class object itself
        return self.canvas
        
        
class BoardSpace(object):
    def __init__(self, position, tags):
        # define length and breadth including out of bounds
        self.position = position
        self.tags = tags
        
        
class Hexagon(BoardSpace):
    def __init__(self, canvas, centre, position, size, fillcolour, outlinecolour, tags, activefillcolour=None, width=1):
        self.canvas = canvas
        self.centre = centre
        self.size = size
        self.fillcolour = fillcolour
        self.outlinecolour = outlinecolour
        self.activefillcolour = activefillcolour if activefillcolour is not None else 'white' # need to work out what this else statement means as seems to be able to be else anything
        self.width = width
        super().__init__(position, tags)
        self.corners = []
        for i in range(0, 6):
            self.corners += Hexagon._get_corner(centre, size, i)

        self.canvas_id = self.canvas.create_polygon(self.corners, 
                                                    outline=self.outlinecolour,
                                                    fill=self.fillcolour, 
                                                    width=self.width, 
                                                    activefill=self.activefillcolour)
        
    @staticmethod
    def _get_corner(centreCoordinates, size, i):
        angleDegrees = 60 * i + 30   # where 60 is the internal angle of the "slice" and 30 is the initial angle of the first corner (taking 0 degrees to be the horizontal line from the centre)
        angleRadians = math.pi / 180 * angleDegrees
        xCoordinate = int(round(centreCoordinates[0] + (size * math.cos(angleRadians))))
        yCoordinate = int(round(centreCoordinates[1] + (size * math.sin(angleRadians))))
        return [xCoordinate, yCoordinate]    # returns a list containing x and y coordinates


import classes.game