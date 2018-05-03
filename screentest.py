import  tkinter as tk

class Game(tk.Tk):    
    '''Creates an instance of Tk and sets basic configuration before switching to the title page'''
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Storm Bowl")
        self.configure(background='#9E332C')
        self.switch_frame(TitlePage)
        self.clubs = []
        self.players = []
        self.fixtures = []
        self.returnfixtures = []

    def switch_frame(self, frame_class):
        '''Destroy current frame and replace with new one'''
        new_frame = frame_class(self)
        if hasattr(self, "_frame"):
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def set_window_size(self, size):
        self.geometry(size)

    def quit_game(self):
        self.destroy()

        
class TitlePage(tk.Frame):
    '''Title page frame where player selects game type'''
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg='#9E332C')
        
        title_label = tk.Label(self, width=15, height=2, bg='#9E332C', fg='white', text="Storm Bowl")
        title_label.config(font=("comic sans ms", 22, "bold"))
        title_label.pack()
        
        Game.set_window_size(master, "300x220")
        
        single_game_button = tk.Button(self, width=20, height=2, highlightbackground='#9E332C', text="New Single Game", command=lambda : master.switch_frame(MatchIntro)).pack()
        league_game_button = tk.Button(self, width=20, height=2, highlightbackground='#9E332C', text="New League Season", command=None).pack()
        quit_button = tk.Button(self, width=20, height=2, highlightbackground='#9E332C', text="Quit Game", command=lambda : Game.quit_game(master)).pack()
        
class MatchIntro(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg='#9E332C')
        
        self.gametype = 'single'
        self.weeknum = 1
        self.hometeam = 'Tim\'s Team'
        self.awayteam = 'The Reds'
        self.homepos = 3
        self.awaypos = 7
        
        title_label = tk.Label(self, bg='#9E332C', fg='white', text='Upcoming Match', font=("Arial", 20, "bold"), pady=10)
        #title_label.config(font=("Arial", 20, "bold"))
        week_label = tk.Label(self, bg='#9E332C', fg='white', text='Round ' + str(self.weeknum), font=("Arial", 16, "bold"))
        hometeam_label = tk.Label(self, bg='#9E332C', fg='white', text=self.hometeam, font=("Arial", 22))
        awayteam_label = tk.Label(self, bg='#9E332C', fg='white', text=self.awayteam, font=("Arial", 22))
        homepos_label = tk.Label(self, bg='#9E332C', fg='white', text='(' + str(self.homepos) + ')')
        awaypos_label = tk.Label(self, bg='#9E332C', fg='white', text='(' + str(self.awaypos) + ')')
        ok_button = tk.Button(self, highlightbackground='#9E332C', text="Continue", pady=20, command=lambda: master.switch_frame(PickSquad))
        
        Game.set_window_size(master, "550x200")
        
        title_label.grid(row=0, column=1)
        week_label.grid(row=1, column=1)
        hometeam_label.grid(row=2, column=0)
        awayteam_label.grid(row=2, column=2)
        homepos_label.grid(row=3, column=0)
        awaypos_label.grid(row=3, column=2)
        ok_button.grid(row=4, column=1)
        
        
class PickSquad(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg='#9E332C')
        
        
        '''
        #lstbox = tk.Listbox(self, selectmode='multiple', bd=0, width=30, height=300)
        lstbox2 = tk.Listbox(self, selectmode='multiple', bd=0, width=10, height=300)
        lstbox2.grid(column=0, row=0)
        #lstbox.grid(column=0, row=0)
        scrollbar = tk.Scrollbar(lstbox2, orient='vertical')
        scrollbar.config(command=lstbox2.yview)
        lstbox2.config(yscrollcommand=scrollbar.set)
        scrollbar.grid(column=0, row=0)
        '''
        self.grid(sticky='nesw')
        self.mainframe()
        
    def mainframe(self):
        myframe = tk.Frame(self)
        self.data = tk.Listbox(myframe, bg='red')
        self.scrollbar = tk.Scrollbar(myframe, orient='vertical', bg='blue',  command=self.data.yview)
        self.data.config(yscrollcommand=self.scrollbar.set)
        #self.scrollbar.config(command=self.data.yview)

        for i in range(100):
            self.data.insert('end', str(i))

        #self.run = tk.Button(self, text='run')
        #self.stop = tk.Button(self, text='stop')

        self.data.pack()
        self.scrollbar.pack()
        #self.data.grid(row=0, column=0, rowspan=4, columnspan=2, sticky='nesw')
        #self.data.columnconfigure(0, weight=1)
        #self.run.grid(row=8, column=0, sticky='ew')
        #self.stop.grid(row=8, column=1, sticky='ew')
        myframe.grid(column=0, row=0)

        #self.scrollbar.grid(row=0, column=2, sticky='ns')
        
        '''
        understand sticky - how the widget is expanded when the cell is larger.
            So 'W' = aligned to left edge of cell
               'E' = aligned to right edge of cell
               'we' = stretched horizontally to fill width of cell
               'ns' = stretched to top and bottom
               default = centred
        try basic code in mac and in windows
        '''
        
        
        
        
        
        
    '''
        players = ['Player1, 17, 9, 4', 'Player2, 17, 9, 4', 'Player3, 17, 9, 4', 'Player4, 17, 9, 4', 'Player5, 17, 9, 4', 'Player6, 17, 9, 4', 'Player7, 17, 9, 4', 'Player8, 17, 9, 4', 'Player9, 17, 9, 4', 'Player10, 17, 9, 4', 'Player11, 17, 9, 4', 'Player12, 17, 9, 4', 'Player13, 17, 9, 4', 'Player14, 17, 9, 4', 'Player15, 17, 9, 4']
        second = ['14, 9, 10', '16, 15, 7', '12, 12, 3', '14, 9, 10', '16, 15, 7', '12, 12, 3', '14, 9, 10', '16, 15, 7', '12, 12, 3', '14, 9, 10', '16, 15, 7', '12, 12, 3', '14, 9, 10', '16, 15, 7', '12, 12, 3']
        
        #for player in players:
            #lstbox.insert('end', player)
            
        for value in second:
            lstbox2.insert('end', value)

    '''    
        
        
        
        
if __name__ == "__main__":
    app = Game()
    app.mainloop()