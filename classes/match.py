
class Match(object):
    def __init__(self, teams):
        print("starting Match initialisation")
        if [team for team in teams if not isinstance(team, str) if team.manager == "human"]:
            self.interactive_match = True
        else:
            self.interactive_match = False
            
        self.hometeam = teams[0]
        self.awayteam = teams[1]
        
        
    def isinteractive(self):
        return self.interactive_match
    
    '''
    set matchstate = "start"
    toss to see who kicks off (need to do this before pick team)
    if interactive:
        call game to draw gameboard
        while loop while matchstate = start
        
    class gameboard
    __init__
        creates basic frame
        defines hex size
        creates canvas
        populates self.hexagons
            --> hexagons have the position attribute e.g. [0,2] which is needed for auto game
    
        
        
    
    '''
    
    
        
        