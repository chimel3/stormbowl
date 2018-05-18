import config
import createclubs
import createplayers
import fixtures
import classes.game
import classes.match
import classes.squadselector
import autopick


def main():
    '''
    This is the function that is returned to after each set of processing has completed as this is where the tkinter mainloop funtion is called.
    '''
    
    config.get_config_data()
    config.start_game()
    '''
    Note that the program enters mainloop but never exits out of it until the root window is closed. Events that are triggered will execute code but still within the mainloop run. Therefore if you are to pause on subsequent screens you need to create your own loop.
    '''
    print("entering mainloop")
    config.game.mainloop()
    

def new_game(game_type):
    '''Create the necessary objects to be able to start a new game of the required type'''
    
    # set the game type in the game object
    classes.game.Game.set_game_type(config.game, game_type)
    
    '''Create the clubs'''
    if game_type == 'single':
        createclubs.create_clubs(2)
    else:
        createclubs.create_clubs(8)
        
    createplayers.create_players()
    fixtures.create_fixture_list()
    
    while config.game.inplay:  # change this to a for loop using rounds variable
        print("starting in-play loop")
        new_round(config.game.roundnum)
        
        config.game.inplay = False   # force this condition for testing
        # complete the round and check for end of game
        # at end of round, set playingstatus to none throughout.
        #classes.game.Game.complete_round(config.game)
        
    

def new_round(roundnum):
    '''
    ABOUT:
    This function runs to complete all of the activities associated with playing a round of fixtures (multiple matches if a league):
    Picking the squad, picking the team, working out who kicks off, set the score, draw the pitch and add the players and then play the match, before updating player stats and also the league table.
    '''
    
    '''
    IDEAS:
    Create a tuple of tuples. Each inner tuple contains the home and away teams, with the outer tuple being a complete list of that round's matches.
    
    for match in matches:   # this means for now each match is serially run. To allow them to happen together I can either explore multithreading (see map and pool) or always run the human game last (only works if a single human player). Then, serially play the computer games but store the result hidden, then play the recording to the human as if done in real time.
        match = match(teams)  # home team first

        calculate league_table   # consider how to handle single game
    
    -->
    Load frame to show the the home team and away team, week number if not a single game and league position if not a single game and not week 1.
    -->
    To get the week number -> game.roundnum holds it directly.
    To get the week's fixtures, need to read classes.game.Game.get_round_fixtures(config.game, weeknumber), where weeknumber comes from the for loop. This hides the complexity in Game class.
    Returns the fixtures list for the week.
    -->
    League position to come later...
    
    ---------

    '''
    
    print("starting new_round")
    # Get the list of fixtures for this round
    fixtures_for_round = classes.game.Game.get_fixtures_for_round(config.game, roundnum)
    
    # sort the list of fixtures so that the human controlled team plays last so can provide a facade of real time activity in future
    fixtures_for_round.append(fixtures_for_round.pop(fixtures_for_round.index(next(fixture for fixture in fixtures_for_round if [team for team in fixture if not isinstance(team, str) if team.manager == "human"]))))
    
    # play each match in turn
    for fixture in fixtures_for_round:
        # Create the match object
        match = classes.match.Match(fixture)
        if classes.match.Match.isinteractive(match):
            # pass name of frame as a string with separate argument list. Otherwise it will evaluate whether all of the parameters are satisfied to call the class's initiator at this stage.
            argument_list = []
            argument_list.append(fixture)
            # show the introduction to match screen
            classes.game.Game.switch_frame(config.game, 'classes.matchintroframe.MatchIntro', argument_list)
            
            # enter into the loop to pause the screen until the user takes action on the present screen
            while config.game.paused:
                config.game.update()

        '''
        # pick the squads for both home and away teams
        if match.hometeam.manager == "computer":
            autopick.autopick_players(match.hometeam)
        else:
            classes.squadselector.PickSquad(match.hometeam)
            
        if match.awayteam.manager == "computer":
            autopick.autopick_players(match.awayteam)
        else:
            classes.squadselector.PickSquad(match.awayteam)
        '''    
    
        # Play the match
        match.play_match(fixture)
    
    '''
    New function to create_match. This is where we pick squads etc.
    Suggest that have a match class.
    It has a score, a ball, two squads, a gameboard, sprites etc
    Try and keep the gamestate in the match class.
    Screen refreshes etc in the gameboard class.
    Gameboard class will also have the hexagon class in same class as it just makes sense to keep these together. Record this in the blog.
    Gameboard is effectively a screen so is called from game class in same way. Therefore the gameboard will have the relevant buttons etc. Need to think about how these change depending on the match. Potentially hide buttons at certain times.
    Need to code a match to be playable by 2 computers...! Or could do this later, but would be fun to do an entire league with computer players only. Could turn it into a management sim!
    '''
    

    

class falseMatch(object):
    '''
    USING TAGS:
    Here is a list of the ways I want to use tags on create_image:
    - to indicate when an object is disabled or enabled. Therefore I can do a tag_bind so that only if I click on an image which is tagged as enabled does it start doing pathfinding etc.
    Note this is different to state = disabled because when it's not the player's turn, the image will be enabled and so not greyed out but the tag needs to say disabled so that I don't allow them to move out of turn.
    - to tag with a uuid of the player object itself for referencing images to players.
    
    Here is a list of potential tags for hexagons:
    - do I have one to indicate which are in-play, which are endzone and which are out of bounds so that I can detect for touchdowns and where not to include for pathfinding?
    
    '''
    '''
    ABOUT:
    Makes sure the images are set correctly depending on whether they are home or away. Set all images to state of normal which means that when you are playing the opponents will be in colour. Therefore only those whose moves are exhausted will be greyed out and they come back to life after the entire go.
    
    Create a new match using Match class. init may have to call all of the subsequent one-off actions until get to the while loop. Not sure yet though. Probably in the init as the subsequent methods will rely on all of these things having been done so init should probably enforce that they are done.
    
    Pick the squads. Needs to be automated for a computer player - def pick_squads
    Decide who kicks off - def toss_coin
    Set the score - def set_score - creates a Score class instance.
    Create a ball - def create_ball - creates a Ball instance.
    Create the pitch - def create_gameboard - class Gameboard instance
    Draw the pitch with just the hexagons - def draw_gameboard. Only hexagons as don't want to draw these again during same match.
    While not gamestate = end_of_match
        Transition to gamestate = start
        if gamestate = all differnet combinations and then call the correct method.
        match.start_match
        play match with varying gamestates etc
    
    '''
    
    '''
    IDEAS:
    Be interesting to try and set the character images according to tags when gameboard is refreshed after every move - see experimeter.py
    set_character_images("home", homeClub)
    set_character_images("away", awayClub)
    
    pick_squad(homeClub)
    pick_squad(awayClub)
    
    simulate a coin toss to decide who kicks off
    
    scoreboard = GameScore(homeClub.name, awayClub.name)
    
    ball = Ball(centre_of_pitch_coordinates)  # centre of pitch coordinates just to start it somewhere since don't know who is kicking off yet.
    
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
    pass

def set_character_images(teamType, team):
    '''
    if teamType == "home":
        set all ImageCurrentActive and ImageCurrentDisabled to backs  #home team at bottom of screen
    else
        set all ImageCurrentActive and ImageCurrentDisabled to fronts
    '''
    pass
    
def pick_squad (club):
    '''
    ABOUT:
    This should open up a screen where it allows the player to select 15 players from their complete list to participate in the next match.
    
    If there are 15 or fewer eligible players (that is non-injured players) then no need to show the screen.
    '''
    
    '''
    IDEAS:
    When select squad, set PlayingStatus to "squad" for those selected.
    Use Availability attribute to decide which are eligible players.
    
    Need to think about how to distinguish between what a human player does and a computer player
    '''
    print("starting pick_squad")
    print(club.manager)
    
class Ball(object):
    '''
    ABOUT:
    Creates a ball object. This is useful as can record where the ball is as well as whether it's in the possession of a player and so does not need to be drawn.
    '''
    
    '''
    IDEAS:
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
    pass
    
class GameScore(object):
    '''
    ABOUT:
    Creates a GameScore object containing home and away team names and scores.
    '''
    
    '''
    INFO:
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
    pass
    
class Gameboard(object):
    '''
    ABOUT:
    Create a gameboard object.
    Contains a draw_board method that can be called after every action to re-draw the board.
    '''
    
    '''
    IDEAS:
    Suggest that I try and create it as a child object of a frame. Look at resizing later on.
    Possibly create a separate frame with the score in it too.
    
    
    def __init__(self, numberDown, numberAcross, hexagon_size)
        This should create and store all of the hexagons in something. Remember that ideally we want to use the placement coordinates e.g. (1,2) to refer to a hexagon.
        Need to consider how to number the OOB hexes.
        
    def draw_board(self):
        This needs to be called after every move to update whether a character is disabled or active (do I also allow them to part move so that they would then have a new movement range showing?)
        
        this will draw the gameboard, referencing the hexagon array and drawing the hexagon with the correct colour and the correct player on top of it if applicable.
        
        
    '''
    pass
        
    
if __name__ == "__main__":
    main()