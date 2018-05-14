import tkinter as tk

class PickSquad(tk.Frame):
    def __init__(self, master, team):
        
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
        pass