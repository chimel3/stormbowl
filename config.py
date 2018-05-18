import classes.game
import json

def start_game():
    global game
    game = classes.game.Game()
    
def get_config_data():
    global teams_data
    global players_data
    global settings_data
    global firstname_data
    global lastname_data
    global board_data
    
    config_data = json.load(open('stormbowl-config.json'))['stormbowl']
    teams_data = config_data['teams']
    players_data = config_data['players']
    settings_data = config_data['settings']
    firstname_data = config_data['playernames']['firstnames']
    lastname_data = config_data['playernames']['lastnames']
    board_data = config_data['board']
    
def start_fixture_list():
    global fixtures
    global returnfixtures   # not implemented initially
    fixtures = []
    returnfixtures = []

    
    
