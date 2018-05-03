import  tkinter as tk

'''

class MasterWindow(tk.Tk):
    Creates an instance of Tk and sets basic configuration before switching to the title page
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Storm Bowl")
        self.configure(background='#9E332C')
        self.switch_frame(TitlePage)
     
    def switch_frame(self, frame_class):
        Destroy current frame and replace with new one
        new_frame = frame_class(self)
        if hasattr(self, "_frame"):
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
    def set_window_size(self, size):
        self.geometry(size)
        
    def quit_game(self):
        self.destroy()
'''        
        
class TitlePage(tk.Frame):
    '''Title page frame where player selects game type'''
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg='#9E332C')
        
        title_label = tk.Label(self, width=15, height=2, bg='#9E332C', fg='white', text="Storm Bowl")
        title_label.config(font=("comic sans ms", 22, "bold"))
        title_label.pack()
        
        classes.game.Game.set_window_size(master, "300x220")
        
        single_game_button = tk.Button(self, width=20, height=2, highlightbackground='#9E332C', text="New Single Game", command=lambda : stormbowl.new_game('single')).pack()
        league_game_button = tk.Button(self, width=20, height=2, highlightbackground='#9E332C', text="New League Season", command=None).pack()
        quit_button = tk.Button(self, width=20, height=2, highlightbackground='#9E332C', text="Quit Game", command=lambda : classes.game.Game.quit_game(master)).pack()

import stormbowl
import classes.game