import classes.club
import config
#import json

def create_clubs(number):
    '''
    ABOUT:
    Creates a list of clubs that it stores in the Game object.
    Whether it is human or computer controlled is in the config file

    '''
    print("starting create_clubs")
    #teams_data = json.load(open('stormbowl-config.json'))['stormbowl']['teams']
    
    # check that there are enough teams in the config file
    if len(config.teams_data) < number:
        pass
    else:
        for i in range(number):
            club = classes.club.Club(config.teams_data[i]['name'], config.teams_data[i]['controller'])
            classes.game.Game.add_club(config.game, club)
            

import classes.game

