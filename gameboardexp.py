import tkinter as tk
from math import pi, cos, sin, sqrt
import random

class GameBoard(tk.Frame): 
    out_of_bounds_size = 4
    
    def __init__(self, master, rows=24, columns=12, size=14):
        self.rows = rows
        self.columns = columns + (2 * self.out_of_bounds_size)
        self.size = size
        tk.Frame.__init__(self, master, borderwidth=10, bg="green")
        
        hexHeight = size * 2
        hexWidth = sqrt(3)/2 * hexHeight
        
        self.canvas = tk.Canvas(self,
                                borderwidth=0,
                                highlightthickness=0,
                                width=(self.columns * hexWidth + (hexWidth / 2)), 
                                height=(self.rows * (hexHeight * 0.75)) + (hexHeight * 0.25),
                                background="blue")
        
        self.canvas.pack()
        self.draw_gameboard(self)
        #self.canvas.bind("<Configure>", self.refresh)
        self.canvas.bind("<Button-1>", self.refresh)
        
        
    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
        
        
        #print(self.canvas.coords((self.canvas.find_withtag('current')))) # this prints out the 6 coordinates of the clicked on hexagon. SO I don't need to store them!
        print(type(self.canvas.itemcget(self.canvas.find_withtag('current'), 'tags')))
        
        #self.canvas.delete('hex')  this is kept here as will do something similar to delete players after user selects a hex to move a player to, or attacks a player.

        
    @staticmethod                
    def draw_gameboard(self):
        '''
        Draws the gameboard i.e. the hexagons. Note that this is a one-time operation as need to keep the colours the same even after a touchdown otherwise it looks like a different pitch.
        '''
        pitchColour = ('#32c032', '#1eab1e', '#3cc83c', '#3c961e', '#0abc22')
        edgeColour = '#e6e6e6'
        endzoneColour = '#8c7373'
                
        for row in range(self.rows):
            for col in range(self.columns):
                
                # check whether this is an out of bounds hex
                if (col < self.out_of_bounds_size) or (
                    col >= self.columns - self.out_of_bounds_size):
                    col -= row // 2  # so column value starts 1 lower for every 2 rows.
                    hexagon = Hexagon(placement_position_to_pixels
                                      (self.size, col, row), 
                                      [col, row], 
                                      self.size)
                    self.canvas.create_polygon(hexagon.corners, 
                                      outline='#566573', 
                                      fill=edgeColour, 
                                      width=0, 
                                      activefill='white',
                                      tags=('outofbounds', 'hex', hexagon.placement))
                    
                # check whether this is an endzone hex
                elif (row == 0) or (row == self.rows - 1):
                    col -= row // 2  # so column value starts 1 lower for every 2 rows.
                    hexagon = Hexagon(placement_position_to_pixels
                                      (self.size, col, row), 
                                      [col, row], 
                                      self.size)
                    self.canvas.create_polygon(hexagon.corners, 
                                          outline='#566573', 
                                          fill=endzoneColour, 
                                          width=0, 
                                          activefill='grey', 
                                          tags=('endzone', 'hex'))
 
                # it must be a pitch hex
                else:  
                    col -= row // 2  # so column value starts 1 lower for every 2 rows.
                    hexagon = Hexagon(placement_position_to_pixels
                                      (self.size, col, row), 
                                      [col, row], 
                                      self.size)
                    self.canvas.create_polygon(hexagon.corners, 
                                          outline='#566573', 
                                          fill=random.sample(pitchColour, 1), 
                                          width=0, 
                                          activefill='green',
                                          tags=('pitch', 'hex'))
        
        

def placement_position_to_pixels(size, column, row):
    '''
    Takes the placement coordinates e.g. [-2, 4] and translates them into pixel coordinates
    '''
    xCoordinate = size * sqrt(3) * (column + row/2)
    yCoordinate = size * 1.5 * row
    '''
    Adjust the coordinates by the relevant number of pixels to account for the fact that the first hexagon can't have its centre-point coordinates at (0,0) because otherwise anything above or to the left of centre would be off the side of the canvas.
    '''
    hexHeight = size * 2
    xCoordinate += ((sqrt(3)/2 * hexHeight) / 2)  # offset by half a hex width
    yCoordinate += size # offset by half the height
    return [xCoordinate, yCoordinate]
    

class Hexagon(object):
    def __init__(self, centreCoordinates, placementPosition, size):
        self.placement = placementPosition
        self.size = size
        self.contains = None
        self.corners = []
        for i in range(0, 6):
            self.corners += Hexagon._get_corner(centreCoordinates, size, i)

    @staticmethod
    def _get_corner(centreCoordinates, size, i):
        angleDegrees = 60 * i + 30   # where 60 is the internal angle of the "slice" and 30 is the initial angle of the first corner (taking 0 degrees to be the horizontal line from the centre)
        angleRadians = pi / 180 * angleDegrees
        xCoordinate = int(round(centreCoordinates[0] + (size * cos(angleRadians))))
        yCoordinate = int(round(centreCoordinates[1] + (size * sin(angleRadians))))
        return [xCoordinate, yCoordinate]    # returns a list containing x and y coordinates


        
'''
CREATES THE GAMEBOARD
'''

master = tk.Tk()
master.title("TFS")
board = GameBoard(master)
board.pack()
master.mainloop()