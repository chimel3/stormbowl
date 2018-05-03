import  tkinter as tk

class MatchIntro(tk.Frame):
    '''Introduces the match, showing information about the next match'''
    def __init__(self, master, teams):
        tk.Frame.__init__(self, master, bg='#9E332C')
        
        self.hometeam = teams[0]
        self.awayteam = teams[1]
        
        # populate variables depending on whether this is a single game or league
        if config.game.gametype == 'single':
            roundtext = 'Single Game'
            hometeam_leagueposition = ''
            awayteam_leagueposition = ''
        else:
            roundtext = 'Round ' + str(config.game.roundnum) 
            hometeam_leagueposition = '(' + ')'   #need to work out how we populate this
            awayteam_leagueposition = '(' + ')'   #need to work out how we populate this
            
         # main title
        title_label = tk.Label(self, bg='#9E332C', fg='white', text='Upcoming Match', font=("Arial", 20, "bold"), pady=10)
        
        # Title to say which round is being played.
        round_label = tk.Label(self, bg='#9E332C', fg='white', text=roundtext, font=("Arial", 16, "bold"))
        
        # Print the names of the clubs playing this match
        hometeam_label = tk.Label(self, bg='#9E332C', fg='white', text=self.hometeam, font=("Arial", 22))
        awayteam_label = tk.Label(self, bg='#9E332C', fg='white', text=self.awayteam, font=("Arial", 22))
        
        # Print the positions in the league of the two clubs
        hometeam_position_label = tk.Label(self, bg='#9E332C', fg='white', text=hometeam_leagueposition)
        awayteam_position_label = tk.Label(self, bg = '#9E332C', fg='white', text=awayteam_leagueposition)
        
        # Create the OK button to move us to the next screen
        ok_button = tk.Button(self, highlightbackground='#9E332C', text="Continue", pady=20, command=lambda: classes.game.Game.switch_frame(classes.picksquad.PickSquad))

        # Set the window size
        classes.game.Game.set_window_size(master, "550x200")
        
        title_label.grid(row=0, column=1)
        round_label.grid(row=1, column=1)
        hometeam_label.grid(row=2, column=0)
        awayteam_label.grid(row=2, column=2)
        hometeam_position_label.grid(row=3, column=0)
        awayteam_position_label.grid(row=3, column=2)
        ok_button.grid(row=4, column=1)
 
        
import stormbowl
import config
import classes.game

'''
fixtures:
A v B
C V DO
B v C
A v DO
A v C
B v DO

3 teams = 3 rounds, 6 matches
n/2(n-1) ==> 3/2(2) = 3 rounds
3 x 2 x 1 = 6 matches

4 teams = 4/2(3) = 6 rounds. But it's not.

16 teams = 15 rounds, 120 matches, so matches = 15 + 14 + 13 etc

n = num of teams (includes day off)
n/2(n-1) = number of matches. 16/2(15) = 120
num of rounds = n-1
'''