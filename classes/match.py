
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
    
    
        
        