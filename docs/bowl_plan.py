'''
Assume single game for now but design with league in mind.
Assume one character type but design for many
'''
Mainline
'''
# could have a form allowing commencement of new single game or league

Creates teams using classes of character and then all characters belonging to a club as contained in a list.
This list is held in a club dictionary that has a "players" key containing this list.
***Need to make sure that the club dictionary contains a reference to the player objects and not a copy so that if the player values change, the value in the club dictionary also changes.***

-> Create 15 characters for club1. For now, hard-code race in a variable. Store in club dictionary.
-> Create 15 characters for club2. Store in club dictionary.
-> Create a match. This should also be a class where pass in the 2 clubs.
    -> 
    
Create clubs - name
Create characters - generic and human
Join characters to club
New match function - match class(teams * 2) - should allow different pitches etc at some point. Starting player chosen here.
New pitch class - called by new match
Create ball - image attribute etc
Draw pitch if human player (can I do it so that computer v computer can play out without drawing pitch - means that game needs to play using hex locations rather than coordinates.)
Pick squad - squad object. Supplements each player with attribute to say if on pitch or not. EXPERIMENT WITH THIS.

players
clubs
squad

Gane configuration stored in JSON? in separate file and read in when needed.
Assume going to be 2 sorts and this is single game.

def new_single_game
def create_clubs(names)
    foreach name in names
        club = Club(name)
        
class 

'''
main:
    '''
    window = tk.Tk()
    window.title("xxx")
    canvas = tk.Canvas()
    
    # at this stage probably need to display a screen to ask what sort of game they want. Not doing this yet. Once finished with the start screen use canvas.delete("all")
    
    new_single_game(config details) # e.g. gametype, club names, player names if I choose to send them.
    
    while not end of game . # need to define this
        new_round(fixtureList, roundNum)   # on basis that each round has matches between all teams
    '''

    
def new_single_game():
    '''
    clubs = create_clubs
    players = create_players (gameType, clubs, race)  # gameType is 'single' or 'league'
    '''
    
def create_clubs(clubnames):
    '''
    clubs = []
    for name in clubnames
        clubs.append(Club(name)) . # creates a clubs list containing each club
    
    return clubs
        
    '''
    
def create_players(gameType, clubs, race, names=None): # allows me to send in list or tuple of names if so choose
    '''
    race_lookup = {'Human': Human, 'Elf': Elf}
    players = []
    for club in clubs:
        if gameType == 'single':
            for 1 to 15:  # 15 is number of players for single game
                players.append(race_lookup[race]{parms...}
                club.add_player_to_club(players[-1])  # adds last player in list to club
                players[-1].add_player_to_club(club.name)
                
    return players
        
    '''
class Club(object):
    '''
    self.name = name
    self.players = []
    self.pitchSize . # this is a future development to allow different sized pitches.
    self.manager .  # either human or computer. Possibly allow human to have a name to allow multiple humans.
    
    def add_player_to_club(player):
        self.players.append(player)
    '''

class Player(self, race):
    '''
    Defines a general character. They will ultimately always be of a certain type though.
    
    def add_player_to_club(club.name):
        self.club = club.name
    '''
    
class Human(character):
    '''
    Add any special abilities here to the object. Should dictate the value of the attributes.
    '''
    
def new_round(fixtureList, roundNum):
    '''
    # fixtureList is some kind of object that holds all of the fixtures on it - maybe some kind of dictionary?
    # roundNum is the round number which allows us to find the correct fixtures for this round
    
    Work out the match schedules into a tuple of tuples? So one outer tuple holding a tuple to represent each match with first item being home team and second item being away team.
    
    for match in matches:   # this means for now each match is serially run. To allow them to happen together I can either explore multithreading (see map and pool) or always run the human game last (only works if a single human player). Then, serially play the computer games but store the result hidden, then play the recording to the human as if done in real time.
        play_match(teams)  # home team first
    
    calculate league_table   # consider how to handle single game
    
        
    '''
    
def play_match(clubs):  # teams is a tuple containing (homeTeam, awayTeam) tuple
    '''
    set_character_images("home", homeClub)
    set_character_images("away", awayClub)
    
    pick_squad(homeClub)
    pick_squad(awayClub)
    
    simulate a coin toss to decide who kicks off
    
    score = GameScore(homeClub, awayClub)
    
    ball = Ball(centre_of_pitch_coordinates)
    
    pitch = GameBoard(teams)
    
    draw gameboard
    
    do while not end of game
        
        pick team and set them up on the gameboard
            Need to think about how to handle experience points. When do they get them for playing?
        
        player kicking off nominate kicker (may not make this a choice in first version)
            set correct player image. May need to record where the ball is so that can make the image correct for the player. Suggest create a ball object that records this.
        
        draw ball
        
        kick off - player kicks ball and receiving team attempt to catch it
        
        do while not touchdown
            code the play
            
            when touchdown call appropriate score method.
            Check for end of game (score of 3)
            
        # note suggests at end of each touchdown and loops back around that player will pick team again from scratch. This seems reasonable as it's like american football where they can pick an entire new team each play. Also makes substitutions more cyclable.
        
    destroy ball
    
    destroy gameboard
    
    manage_injuries - those that were injured in the game should have Availability set during the game and recoveryTime set to 1 higher than the number of games missed (since next stage will reduce it by 1 immediately:
        - reduce RecoveryTime by 1 where not already 0.
        - if reaches 0 then set Availability to "available"
        
    Set PlayingStatus to "none"
    
    display score and wait for acknowledgement # might need to do this later as don't want computer teams to have to acknowledge.
        
    '''

def set_character_images(teamType, team):
    '''
    if teamType == "home":
        set all ImageCurrentActive and ImageCurrentDisabled to backs  #home team at bottom of screen
    else
        set all ImageCurrentActive and ImageCurrentDisabled to fronts
    '''
    
def pick_squad (club):
    '''
    Need to think about how to distinguish between what a human player does and a computer player
    
    count number of available players. if <=15 then skip this stage and continue since no need to pick.
    Set each player's PlayingStatus to "squad".
    
    otherwise need to display a form and allow them to pick them.
    For those that are picked set PlayingStatus to "squad". Others remain at "none"
    '''
    
class Ball(object):
    '''
    def __init__(coordinates):
        ball.image = hardcoded image
        ball.position = coordinates
        ball.possession = can either be true for with a player so don't have to draw it or false so that know it needs to be drawn. Or if better, could record the player with it or placement coordinates or none if not.
        
    def draw_ball(ball):
        if ball.possession = with player:
            pass  # or may need to remove the ball picture from the pitch if not already done beforehand.
        else:
            draw ball on canvas
    '''
    
class GameScore(object):
    '''
    def __init__ (homeTeam, awayTeam):
        self.homeTeam = homeTeam
        self.homeScore = 0
        self.awayTeam = awayTeam
        self.awayScore = 0
        
    def home_touchdown(self):
        self.hometeam += 1
        
    def away_touchdown(self):
        self.awayteam += 1
    '''
    
class Gameboard(object):
    '''
    __init__
        This should create and store all of the hexagons in something. Remember that ideally we want to use the placement coordinates e.g. (1,2) to refer to a hexagon.
        Need to consider how to number the OOB hexes.
        
    def draw_board(self):
        THis needs to be called after every move to update whether a character is disabled or active (do I also allow them to part move so that they would then have a new movement range showing?)
        
        this will draw the gameboard, referencing the hexagon array and drawing the hexagon with the correct colour and the correct player on top of it if applicable.
        
        
    '''
    
