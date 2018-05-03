import tkinter as tk
from math import pi, cos, sin, sqrt
import random

class GameBoard(tk.Frame): 
    out_of_bounds_size = 4
    '''
    these images do not belong here as they will depend on the characters but here just to allow me to try out creating the characters on the board
    '''
    
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
        self.hexagons = self.draw_gameboard(self)
        #self.canvas.bind("<Configure>", self.refresh)
        #self.canvas.bind("<Button-1>", self.refresh_gameboard)
    
    
    def board_click(self, event):
        '''
        Work out whether I have clicked on a hex or a character or a ball.
        This could be at the start of a game or restart where there are no players and need to position them all, or during the game when I am moving players.
        Feels like I need a gamestate variable that holds what state the game is in and this is available throughout. Either it's global or it's held in the main turn and dictates what happens.
        
        
        
        Gamestates:
        
        start - start here and in this phase until 11 players are placed or no players left to place. In this phase you select a player from a list and select a hex to place them on. Can't undo it for now as makes it hard. Need a form to select the player.
        When finished laying out the players, change gamestate to kickoff_select_player
        
        kickoff_select_player - have to click on a player to nominate them as the kicking player. At this stage no change of mind allowed as can't be arsed to code it yet. Once selected changes to kickoff_select_target.
        
        kickoff_select_target - they can nominate a hex or player to kick it to. Game calculates the success of the kick (maybe a ball_iskicked method of the ball class). When finished and calculated whether anyone has picked the ball up, redraw the board and move gamestate to select_player_to_move
        
        select_player_to_move - in this game state each player that you hover over should show the possible movement options. Waits for you to click a player. THerefore all player objects drawn should be labelled as a player so only responds to player clicks and not hex clicks. Opposing team should be disabled so can't click on them. THis may present some interesting challenges when want to attack a player if can't click on disabled players. Either don't disable opposing players but have a label for home/away (which seems bad as have to feed this into the code) or re-enable opposing players during the select_player_to_attack phase and disable own players. This seems better. Set gamestate to select_move_location.
        
        select_move_location - only respond to empty hex's (so will need to label appropriately and test whether person can click on hex beneath a person. If they can then I will need to check that the clicked hex does not share centre coordinates with a player and if it does restart the click event.) Do I allow them to back out of this by doing something (maybe clicking on the same player again?). Could do this by adding a temporary label to the selected player e.g. 'selected' that is removed after they move or after they are clicked on again. If they move to a hex containing the ball they automatically pick it up. Move player and then change gamestate back to select_player_to_move.
        Note that if they are moving out of an opponent's DMZ that a tackle can be made. Tackled player is prone in the hex in which they were about to leave the DMZ.
        If a player moves into opposition endzone with the ball then touchdown is scored. Move gamestate to touchdown
        
        touchdown - update score, remove players from board and either restart match or end it.
        
        end_of_move_phase - this is set when all players have moved, or can be called manually even if a player hasn't moved (so need a button on the board which disappears or appears depending on state of game).
        This phase is transient and just allows us to start the action phase. Set gamestate to select_player_for_action. Also evaluate all players at this stage. if any of them can't take any action then disable them so can't be selected for an action.
        
        select_player_for_action - allows clicking of any of your players. Once selected transition to select_action gamestate and add temp label to player to indicate that they are selected.
        Always a button to end action phase early.
        
        select_action - allow clicking of same player again to cancel and switch back to select_player_for_action. Otherwise select from action buttons for the player. At this stage it needs to understand the player context to determine which actions can be taken. So if they have the ball they can throw, kick or handoff as well as tackle or attack. Set gamestate to the appropriate action and disable the action buttons. 
        
        attack_player - select a player in the DMZ that can be attacked and then carry out the attack. Disable player at end and set gamestate to select_player_for_action. If ball changes hands here then check for touchdown.
        
        tackle_ball_player - automatically attempts to tackle the person with the ball. The ball player had to be in the DMZ to allow this option to be taken. Disable player and set gamestate to select_player_for_action at end having taken consideration of any changes in ball possession and position. If ball changes hands here then check for touchdown.
        
        throw_ball - show all possible hexes (do I include out of bounds?) and allow player to select one of them. Disable player and set gamestate to select_player_for_action. If ball changes hands here then check for touchdown.
        
        kick_ball - show all possible hexes and allow player to select one of them. Disable player and set gamestate to select_player_for_action. If ball changes hands here then check for touchdown.
        
        select_substitute - this is part of reconciliation and is only transitioned to if a team has fewer than 11 players on the pitch and has others it can bring on and a subs place on pitch is available. Presents list of substitutes but can decide to select none of them. When select a player set gamestate to place_substitute
        
        place_substitute - select a hex in appropriate place to bring player on at. Transition gamestate back to select_substitute if still fewer than 11 players and one of the 4 sub spaces is free.
        
        end_of_action_phase - transient phase to allow change of enabled teams, righting of prone players. Gamestate back to select_player_to_move for other team.
        
        end_of_match - set after scoring the final touchdown and allows us to exit the while loop.
        '''
    '''    
    def refresh_gameboard(self, event):
        
        global activeimage
        global inactiveimage
        activeimage = tk.PhotoImage(file="sample.gif")
        inactiveimage = tk.PhotoImage(file="samplegrey-2.gif")
        #print(self.canvas.coords((self.canvas.find_withtag('current')))) # this prints out the 6 coordinates of the clicked on hexagon. SO I don't need to store them!
        #print(type(self.canvas.itemcget(self.canvas.find_withtag('current'), 'tags')))
        
        #self.canvas.delete('hex')  this is kept here as will do something similar to delete players after user selects a hex to move a player to, or attacks a player.
        #print(self.canvas.find_withtag('current')[0])  # this returns the integer of the canvas ID. We have a match we can do!
        print(self.canvas.find_withtag('current')[0])
        hexagon = list(filter(lambda x: x.canvas_id == self.canvas.find_withtag('current')[0], self.hexagons))[0]
        
        for hexagon in self.hexagons:
            if self.canvas.find_withtag('current')[0] == hexagon.canvas_id:
                print(hexagon.position)
                #print(image1)
                #self.canvas.create_image(hexagon.centre[0], hexagon.centre[1], image=image1)
               
        new_player = Playersprite(self.canvas, 
                                  hexagon.centre, 
                                  activeimage,
                                  inactiveimage, 
                                  "normal")
        #print(new_player.canvas_id)
        
        #if self.canvas.find_withtag('current')[0] in self.hexagons.canvas_id:
        #for hexagon.canvas_id in self.hexagons:
        #    if filter()
        
        
        # uses list comprehension to return the hexagon from the object list - self.hexagons - that matches the canvas ID of the hexagon that has been clicked on. Because the returned result is always an array, and I know there can only be a single matching hexagon, I have to get the [0] element, and return its "position" attribute.
        print([hexagon for hexagon in self.hexagons if hexagon.canvas_id == self.canvas.find_withtag('current')[0]][0].position)
        #print(matching[0].position)
        
        print(list(filter(lambda x: x.canvas_id == self.canvas.find_withtag('current')[0], self.hexagons))[0].position)
        #print(matching[0].position)
        
        '''
        
    @staticmethod                
    def draw_gameboard(self):
        '''
        Draws the gameboard i.e. the hexagons. Note that this is a one-time operation as need to keep the colours the same even after a touchdown otherwise it looks like a different pitch.
        '''
        pitchColour = ('#32c032', '#1eab1e', '#3cc83c', '#3c961e', '#0abc22')
        edgeColour = '#e6e6e6'
        endzoneColour = '#8c7373'
        boardhexagons = []
                
        for row in range(self.rows):
            for col in range(self.columns):
                
                # check whether this is an out of bounds hex
                if (col < self.out_of_bounds_size) or (
                    col >= self.columns - self.out_of_bounds_size):
                    col -= row // 2  # so column value starts 1 lower for every 2 rows.
                    boardhexagons.append(Hexo(self.canvas, 
                                   placement_position_to_pixels(self.size, col, row), 
                                   [col, row], 
                                   self.size, 
                                   edgeColour, 
                                   '#566573', 
                                   ('outofbounds', 'hex'), 
                                   'white'))
                    
                # check whether this is an endzone hex
                elif (row == 0) or (row == self.rows - 1):
                    col -= row // 2  # so column value starts 1 lower for every 2 rows.
                    boardhexagons.append(Hexo(self.canvas, 
                                   placement_position_to_pixels(self.size, col, row), 
                                   [col, row], 
                                   self.size, 
                                   endzoneColour, 
                                   '#566573', 
                                   ('endzone', 'hex'), 
                                   'grey'))
 
                # it must be a pitch hex
                else:  
                    col -= row // 2  # so column value starts 1 lower for every 2 rows.
                    boardhexagons.append(Hexo(self.canvas, 
                                   placement_position_to_pixels(self.size, col, row), 
                                   [col, row], 
                                   self.size, 
                                   random.sample(pitchColour, 1), 
                                   '#566573', 
                                   ('pitch', 'hex'), 
                                   'green'))
        return boardhexagons

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
    
    
class Hexo(object):
    def __init__(self, canvas, centre, position, size, fillcolour, outlinecolour, tags, activefillcolour=None, width=1):
        
        self.canvas = canvas
        self.centre = centre  # this is a list [x,y]
        self.position = position  #position is a list [0,0].
        self.size = size
        self.fillcolour = fillcolour
        self.outlinecolour = outlinecolour
        self.width = width
        self.activefillcolour = activefillcolour if activefillcolour is not None else fill # need to work out what this else statement means as seems to be able to be else anything
        self.tags = tags
        self.corners = []
        for i in range(0, 6):
            self.corners += Hexo._get_corner(centre, size, i)

        self.canvas_id = self.canvas.create_polygon(self.corners, 
                                                    outline=self.outlinecolour,
                                                    fill=self.fillcolour, 
                                                    width=self.width, 
                                                    activefill=self.activefillcolour)

    @staticmethod
    def _get_corner(centreCoordinates, size, i):
        angleDegrees = 60 * i + 30   # where 60 is the internal angle of the "slice" and 30 is the initial angle of the first corner (taking 0 degrees to be the horizontal line from the centre)
        angleRadians = pi / 180 * angleDegrees
        xCoordinate = int(round(centreCoordinates[0] + (size * cos(angleRadians))))
        yCoordinate = int(round(centreCoordinates[1] + (size * sin(angleRadians))))
        return [xCoordinate, yCoordinate]    # returns a list containing x and y coordinates


class Playersprite(object):
    def __init__(self, canvas, centre, activeimage, disabledimage, state):
        self.canvas = canvas
        self.centre = centre
        self.activeimage = activeimage
        self.disabledimage = disabledimage
        self.state = state
        
        self.canvas_id = self.canvas.create_image(self.centre[0],
                                                  self.centre[1],
                                                  image=self.activeimage,
                                                  disabledimage=self.disabledimage,
                                                  state=self.state)
        
        
'''
CREATES THE GAMEBOARD
'''

master = tk.Tk()
master.title("TFS")
board = GameBoard(master)
board.pack()
board.canvas.bind("<Button-1>", board.refresh_gameboard)
master.mainloop()