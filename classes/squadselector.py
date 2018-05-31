import tkinter as tk
import operator
from tkinter import ttk
from tkinter import messagebox

class PickSquad(tk.Frame):
    def __init__(self, master, club):
        
        tk.Frame.__init__(self, master, bg='#9E332C')
        print("starting PickSquad initialisation")

        # pause game
        config.game.pause_game()

        # the team is currently contained in a list, so let's get it out of that as it's awkward to deal with
        club = club[0]

        # Set the window size
        classes.game.Game.set_window_size(master, "600x400")

         # main title
        title_label = tk.Label(self, bg='#9E332C', fg='white', text='Pick Squad', font=("Arial", 20, "bold"), pady=10)
        title_label.grid(row=0, column=1)

        # create the treeview and scrollbar        
        self.player_tree = ttk.Treeview(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.player_tree.yview)

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
                # note that uuid is in the values but is not displayed in the treeview
                self.player_tree.insert("", 'end', iid=player.uuid, text=player.name, values=(player.movement, player.attack, player.defense, player.strength, player.toughness, player.resilience, player.throwing, player.kicking, player.agility, player.catching), tags=("deselected"))
 
        # display treeview and scrollbar
        self.player_tree.grid(row=1, column=0, columnspan=10)
        self.scrollbar.grid(row=1, column=11, sticky='ns')
        self.player_tree.configure(yscrollcommand=self.scrollbar.set)

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
        #print(self.player_tree.item(item, "values")[-1]) # where [-1] gets us the uuid
        if self.player_tree.item(item, "tags")[0] == 'deselected':
            self.player_tree.item(item, tags="selected")
        else:
            self.player_tree.item(item, tags="deselected")

        # Colour code all selected players as white text on blue
        self.player_tree.tag_configure("selected", background='blue', foreground='white')
        self.player_tree.tag_configure("deselected", background='white', foreground='black')

    def validate_squad(self):
        if len(self.player_tree.tag_has("selected")) > 15:
            messagebox.showerror("Too many selected", "You have selected more than 15 players for the match day squad. Please deselect some and try again")
        elif len(self.player_tree.tag_has("selected")) < 15:
            if (messagebox.askyesno("Too few selected", "You have selected fewer than 15 players for the match day squad. Is that right?")):
                self.update_player_attributes()
        else:
            self.update_player_attributes()

    def update_player_attributes(self):
        selected_players = self.player_tree.tag_has("selected")
        for uuid in selected_players:
            config.game.update_player_playing_status(uuid, "squad")

        config.game.continue_game()



import classes.game
import config


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
