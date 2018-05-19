import tkinter as tk

class PickSquad(tk.Frame):
    def __init__(self, master, club):
        
        '''    
        Pick squads
        -->
        If <= 15, all players are highlighted by default. If not, ideally keep squad same as last match as a default.
        Load frame to show the match details at the top, with the list of players (and hopefully their attributes). Each player is black text on white. You then click to add them to the squad (white text on black). Unavailable players are red writing on white.
        When complete, check number of selected.
        If < 15, warn that fewer than 15 in squad and OK to continue.
        If > 15, warn that too many in squad, disabled the OK.
        If 15, continue.
        -->
        For computer players:
        Pick at random.
        '''
        tk.Frame.__init__(self, master, bg='#9E332C')
        print("starting PickSquad initialisation")

        # the team is currently contained in a list, so let's get it out of that as it's awkward to deal with
        club = club[0]

                # Set the window size
        classes.game.Game.set_window_size(master, "500x600")

        # Create the scrollbar
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack( side = 'right', fill = 'y' )

        # Get a list of eligible players for the club
        player_name_list = tk.Listbox(self, yscrollcommand = scrollbar.set )
        for player in club.players:
            if player.availability == 'available':
                player_name_list.insert('end', player.name)

        player_name_list.pack( side = 'left', fill = 'both' )
        scrollbar.config( command = player_name_list.yview )

        #ok_button = tk.Button(self, highlightbackground='#9E332C', text="Continue", pady=20, command=lambda : classes.game.Game.restart_game(config.game))

        
import classes.game



