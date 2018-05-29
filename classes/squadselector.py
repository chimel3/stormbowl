import tkinter as tk
import operator
from tkinter import ttk

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
        classes.game.Game.set_window_size(master, "600x500")

         # main title
        title_label = tk.Label(self, bg='#9E332C', fg='white', text='Pick Squad', font=("Arial", 20, "bold"), pady=10)
        title_label.grid(row=0, column=1)
        
        self.player_tree = ttk.Treeview(self)
        self.player_tree["columns"] = ('movement', 'attack', 'defense', 'strength', 'toughness', 'resilience', 'throwing', 'kicking', 'agility', 'catching')
        self.player_tree.heading('#0', text="Name")
        self.player_tree.column("movement", width=35)
        self.player_tree.heading("movement", text="MOV")
        self.player_tree.column("attack", width=35)
        self.player_tree.heading("attack", text="ATT")
        self.player_tree.column("defense", width=35)
        self.player_tree.heading("defense", text="DEF")
        self.player_tree.column("strength", width=35)
        self.player_tree.heading("strength", text="STR")
        self.player_tree.column("toughness", width=35)
        self.player_tree.heading("toughness", text="TOU")
        self.player_tree.column("resilience", width=35)
        self.player_tree.heading("resilience", text="RES")
        self.player_tree.column("throwing", width=35)
        self.player_tree.heading("throwing", text="THR")
        self.player_tree.column("kicking", width=35)
        self.player_tree.heading("kicking", text="KIC")
        self.player_tree.column("agility", width=35)
        self.player_tree.heading("agility", text="AGI")
        self.player_tree.column("catching", width=35)
        self.player_tree.heading("catching", text="CAT")
        for player in club.players:
            if player.availability == 'available':
                #player_tree.insert(' ', 'end', text=player.name, values=(player.movement, player.attack, player.defense, player.strength, player.toughness, player.resilience, player.throwing, player.kicking, player.agility, player.catching))
                self.player_tree.insert("", 'end', text=player.name, values=(4, 3, 3, 4, 3, 7, 8, 9, 7, 10), tags=("deselected"))
                #self.player_tree.tag_configure("deselected", background="white")

        self.player_tree.grid(row=1, column=0, columnspan=10)

        # Display key and OK button
        empty_row = tk.Label(self, bg='#9E332C')
        empty_row.grid(row=2, column=0)
        self.keyframe = tk.LabelFrame(self, text="Key", bg='#9E332C', fg='white', font=("Arial", 12, "bold"), padx=5, pady=5)
        self.keyframe.grid(row=3, column=0)
        self.key_deselected = tk.Label(self.keyframe, background="white", foreground="black", text="deselected")
        self.key_selected = tk.Label(self.keyframe, background="blue", foreground="white", text="selected")
        self.key_deselected.grid(row=4, column=0)
        self.key_selected.grid(row=5, column=0)
        self.ok_button = tk.Button(self, highlightbackground='#9E332C', text="Finished", padx=12, pady=12, command=self.validate_squad)
        self.ok_button.grid(row=3, column=1)
        self.player_tree.bind('<Button-1>', self.select_player)
        
    def select_player(self, event):
        item = self.player_tree.identify('item', event.x, event.y)
        print("clicked on ", self.player_tree.item(item, "text"))
        print(self.player_tree.item(item, "tags"))
        if self.player_tree.item(item, "tags")[0] == 'deselected':
            self.player_tree.item(item, tags="selected")
        else:
            self.player_tree.item(item, tags="deselected")

        # Colour code all selected players as white text on blue
        self.player_tree.tag_configure("selected", background='blue', foreground='white')
        self.player_tree.tag_configure("deselected", background='white', foreground='black')

    def validate_squad(self):
        sels = self.player_tree.tag_has("selected")
        print(len(sels))

import classes.game


'''
        # Create the scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack( side = 'right', fill = 'y' )

        # Get a list of eligible players for the club
        self.player_name_list = tk.Listbox(self, yscrollcommand = self.scrollbar.set )
        #self.player_name_list = tk.Listbox(self, yscrollcommand = self.yscroll1 )
        #self.player_movement_list = tk.Listbox(self, yscrollcommand = self.yscroll2 )
        for player in club.players:
            if player.availability == 'available':
                player_stats = operator.attrgetter('movement', 'attack', 'defense', 'strength', 'toughness', 'resilience', 'throwing', 'kicking', 'agility', 'catching')(player)
                # insert delimiter between the stats for readability
                stats_string = ' | '.join(str(s) for s in player_stats)
                self.player_name_list.insert('end', stats_string)
                #self.player_movement_list.insert('end', player.movement)

        self.player_name_list.pack( side = 'left', fill = 'both' )
        #self.player_movement_list.pack( side = 'left', fill = 'both' )
        self.scrollbar.config( command = self.player_name_list.yview )
        #self.scrollbar.config( command = self.yview )

        #ok_button = tk.Button(self, highlightbackground='#9E332C', text="Continue", pady=20, command=lambda : classes.game.Game.restart_game(config.game))
       
  
    def yscroll1(self,*args):
        if self.player_movement_list.yview() != self.player_name_list.yview():
            self.player_movement_list.yview_moveto(args[0])
        self.scrollbar.set(*args)

    def yscroll2(self,*args):
        if self.player_name_list.yview() != self.player_movement_list.yview():
            self.player_name_list.yview_moveto(args[0])
        self.scrollbar.set(*args)

    def yview(self, *args):
        self.player_name_list.yview(*args)
        self.player_movement_list.yview(*args)
'''
