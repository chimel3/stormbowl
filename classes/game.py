import  tkinter as tk
import classes.titleframe
import classes.matchintroframe
import classes.squadselector

class Game(tk.Tk):    
    '''Creates an instance of Tk and sets basic configuration before switching to the title page'''
    def __init__(self):
        print("starting Game initialisation")
        tk.Tk.__init__(self)
        self.title("Storm Bowl")
        self.configure(background='#9E332C')
        self.inplay = self.game_started()
        self.continue_game()
        self.roundnum = 1
        self.switch_frame('classes.titleframe.TitlePage')
        self.clubs = []
        self.players = []
        self.fixtures = []
        self.returnfixtures = []
     
    def pause_game(self):
        print("game paused")
        self.paused = True
    
    def continue_game(self):
        print("game restarted")
        self.paused = False
    
    def game_started(self):
        '''Set the game to started'''
        return True
    
    def game_finished(self):
        '''Set the game to finished'''
        return False
    
    def switch_frame(self, frame_class, params=None):
        '''
        Destroy current frame and replace with new one.
        frame_class to be passed as a string as otherwise the calling code will attempt to evaluate conformity with the parameters defined in the __init__ of the class we call. This will not work when it requires more than self and master.
        Any *args passed through MUST BE a single list type which can then contain all of the arguments.
        '''
        print("starting switch_frame")
        # open up the new frame with or without additional arguments     
        if params is None:
            new_frame = eval(frame_class)(self)
        else:
            new_frame = eval(frame_class)(self, params)
        
        # destroy any existing frame
        if hasattr(self, "_frame"):
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
    def set_window_size(self, size):
        self.geometry(size)
        
    def quit_game(self):
        self.destroy()
        
    def set_game_type(self, gametype):
        self.gametype = gametype
        
    def add_club(self, club):
        self.clubs.append(club)
        #print("adding club to game: " + str(club.name))
        
    def add_player(self, player):
        self.players.append(player)
        #print("adding player to game: " + str(player.name))

    def update_player_playing_status(self, player_uuid, new_status):
        thisplayer = next(player )
        
    def complete_round(self):
        self.roundnum += 1
        # Set inplay property to False if all fixtures completed
        if (len(clublist) % 2 and self.roundnum > len(self.clubs)) or (not len(clublist) % 2 and self.roundnum == len(self.clubs)):
            self.inplay = self.game_finished()
        
    def add_fixture(self, hometeam, awayteam):
        self.fixtures.append((hometeam, awayteam))
        
    def add_returnfixture(self, hometeam, awayteam):
        self.returnfixtures.append((hometeam, awayteam))

    def fixtures_per_round(self, number):
        '''This prevents having to work it out every round'''
        self.fixturesinround = number
        
    def get_fixtures_for_round(self, roundnumber):
        '''returns the fixtures associated with that round'''
        fixtures = []
        for itemnumber in range(roundnumber -1 * self.fixturesinround, roundnumber * self.fixturesinround):  # remembering that the upper number of range needs to be 1 higher than want to return
            fixtures.append(self.fixtures[itemnumber])
            
        return fixtures
        
