import config
import random
import math
import classes.play


class Match(object):
    
    out_of_bounds_size = 4
    
    def __init__(self, teams):
        print("starting Match initialisation")
        if [team for team in teams if not isinstance(team, str) if team.manager == "human"]:
            self.interactive_match = True
        else:
            self.interactive_match = False
            
        print("interactive: " + str(self.isinteractive()))
            
        self.hometeam = teams[0]
        self.awayteam = teams[1]
        self.rows_in_play = self.hometeam.pitchsize[0]
        self.columns_in_play = self.hometeam.pitchsize[1] + (2 * self.out_of_bounds_size)
        self.gamestate = None
            
    
    def isinteractive(self):
        '''returns whether this is an interactive - True match or not - False'''
        return self.interactive_match
    
    
    def play_match(self, teams):
        '''Initiation part of the match itself. If there is a human player it creates the frame'''
        print("starting play_match")

        if self.isinteractive():
            argument_list = []
            argument_list.append(self.rows_in_play)
            argument_list.append(self.columns_in_play)
            argument_list.append(config.board_data['boardspacesize'])
            self.pitch = config.game.switch_frame('classes.play.Pitch', argument_list)
            self.canvas = self.pitch.create_canvas()
            
        self.change_gamestate('self.gamestate_toss_coin')
        
    def change_gamestate(self, state):
        '''Function to transition to a new gamestate'''
        eval(state)()
        
    
    def gamestate_toss_coin(self):
        '''decides who kicks off'''
        print("starting gamestate_toss_coin")
        coin_toss_list = []
        coin_toss_list.append(self.hometeam)
        coin_toss_list.append(self.awayteam)
        self.activeteam = random.choice(coin_toss_list)
        self.change_gamestate('self.gamestate_create_boardspaces')
        
    
    def gamestate_create_boardspaces(self):
        '''creates the boardspaces as either logical in-memory constructs for computer vs computer games or as visible hexagons if there is a human player'''
        self.boardspaces = []
        for row in range(self.rows_in_play):
            for column in range(self.columns_in_play):
                
                # check for out of bounds hexagon
                if (column < self.out_of_bounds_size) or (
                    column >= self.columns_in_play - self.out_of_bounds_size):
                    column -= row // 2  # so column value starts 1 lower for every 2 rows
                    
                    if self.isinteractive():
                        self.boardspaces.append(classes.play.Hexagon(self.canvas, 
                                                       Match._placement_position_to_pixels(config.board_data['boardspacesize'], column, row),
                                                       [column,row],
                                                       config.board_data['boardspacesize'],
                                                       config.board_data['colours']['outofbounds'],
                                                       config.board_data['colours']['outline'],('outofbounds', 'hex'),
                                                       config.board_data['activefillcolours']['outofbounds']))
                    else:
                        self.boardspaces.append(classes.play.BoardSpace([column,row], 
                                                           ('outofbounds', 'hex')))
                    
                # check for endzone hexagon
                elif (row == 0) or (row == self.rows_in_play - 1):
                    column -= row // 2  # so column value starts 1 lower for every 2 rows

                    if self.isinteractive():
                        self.boardspaces.append(classes.play.Hexagon(self.canvas, 
                                                   Match._placement_position_to_pixels(config.board_data['boardspacesize'], column, row),
                                                   [column,row],
                                                   config.board_data['boardspacesize'],
                                                   config.board_data['colours']['endzone'],
                                                   config.board_data['colours']['outline'], ('endzone', 'hex'),
                                                   config.board_data['activefillcolours']['endzone']))
                    else:
                        self.boardspaces.append(classes.play.BoardSpace([column,row],
                                                           ('endzone', 'hex')))

                # it's a pitch hexagon
                else:  
                    column -= row // 2  # so column value starts 1 lower for every 2 rows.

                    if self.isinteractive():
                        self.boardspaces.append(classes.play.Hexagon(self.canvas, 
                                                   Match._placement_position_to_pixels(config.board_data['boardspacesize'], column, row),
                                                   [column,row],
                                                   config.board_data['boardspacesize'],
                                                   random.sample(config.board_data['colours']['pitch'], 1),
                                                   config.board_data['colours']['outline'], ('pitch', 'hex'),
                                                   config.board_data['activefillcolours']['pitch']))
                    else:
                        self.boardspaces.append(classes.play.BoardSpace([column,row],
                                                           ('pitch', 'hex')))
                      
    
    @staticmethod
    def _placement_position_to_pixels(size, column, row):
        '''takes the placement coordinates e.g. [-2, 4] and translates them into pixel coordinates'''
        xCoordinate = size * math.sqrt(3) * (column + row/2)
        yCoordinate = size * 1.5 * row
        '''
        Adjust the coordinates by the relevant number of pixels to account for the fact that the first hexagon can't have its centre-point coordinates at (0,0) because otherwise anything above or to the left of centre would be off the side of the canvas.
        '''
        hexHeight = size * 2
        xCoordinate += ((math.sqrt(3)/2 * hexHeight) / 2)  # offset by half a hex width
        yCoordinate += size # offset by half the height
        return [xCoordinate, yCoordinate]   


    
    
    
        
        