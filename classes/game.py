import  tkinter as tk
import classes.titleframe

class Game(tk.Tk):    
    '''Creates an instance of Tk and sets basic configuration before switching to the title page'''
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Storm Bowl")
        self.configure(background='#9E332C')
        self.inplay = self.game_started()
        self.roundnum = 1
        self.switch_frame(classes.titleframe.TitlePage)
        self.clubs = []
        self.players = []
        self.fixtures = []
        self.returnfixtures = []
     
    def game_started(self):
        '''Set the game to started'''
        return True
    
    def game_finished(self):
        '''Set the game to finished'''
        return False
    
    def switch_frame(self, frame_class):
        '''Destroy current frame and replace with new one'''
        new_frame = frame_class(self, *args)
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
        
