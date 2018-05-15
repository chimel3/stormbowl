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
        
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack( side = 'right', fill = 'y' )

        mylist = tk.Listbox(self, yscrollcommand = scrollbar.set )
        for line in range(100):
            mylist.insert('end', "This is line number " + str(line))

        mylist.pack( side = 'left', fill = 'both' )
        scrollbar.config( command = mylist.yview )


app = Game()
app.mainloop()