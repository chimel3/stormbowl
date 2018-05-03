
class Match(teams):
    def __init__(self):
        if [team for team in teams if not isinstance(team, str) if team.manager == "human"]:
            self.interactive_match = True
        else:
            self.interactive_match = False
            
        self.hometeam = team[0]
        self.awayteam = team[1]
        
        
    def isinteractive(self):
        return self.interactive_match
    
    
        
        