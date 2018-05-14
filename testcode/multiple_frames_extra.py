import tkinter as tk
from math import pi, cos, sin, sqrt
import random
import sys
import time

    

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.inplay = True
        self.unpause_game()
        self.title("Title window")
        self.geometry("300x300")
        self.switch_frame(StartPage)
        
    def switch_frame(self, frame_class):
        '''destroy current frame and replace with new one'''
        new_frame = frame_class(self)
        print(str(getattr(self, "_frame", "noframe")))
        if hasattr(self, "_frame"):
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
    def set_window_size(self, size):
        self.geometry(size)
        
    def run_game(self):
        while self.inplay:
            fun_one()
            self.switch_frame(WinTwo)
            #self.update()
            fun_two()
            self.pause_game()
            while self.pause:
                self.update()
                self.update_idletasks()
                
            self.switch_frame(StartPage)
            self.update()
            fun_three()
            self.pause_game()
            while self.pause:
                self.update()
                self.update_idletasks()
                
            self.inplay = False
            
    def pause_game(self):
        print("pausing game")
        self.pause = True
        
    def unpause_game(self):
        print("unpausing game")
        self.pause = False
        

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #master.geometry("150x150")
        App.set_window_size(master, "170x250")
        master.title("Start page")
        btn1 = tk.Button(self, text="Open window 2", command=lambda : master.run_game())
        btn2 = tk.Button(self, text="Open window 3", command=lambda : master.run_game())
        btn1.pack()
        btn2.pack()
        print("finished StartPage")
        
def testprint():
    print("testprint")
        
class WinTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #master.geometry("450x150")
        App.set_window_size(master, "350x50")
        master.title("Window 2")
        btn3 = tk.Button(self, text="Return to title page", command=lambda : master.unpause_game())
        btn3.pack()
        print("Finished WinTwo")
        
class WinThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        App.set_window_size(master, "400x400")
        #master.geometry("150x450")
        master.title("Window 3")
        btn4 = tk.Button(self, text="Return to title page", command=lambda : master.unpause_game())
        btn4.pack()
        print("Finished WinThree")
        
def fun_one():
    print("running fun_one")
    for _ in range(1,100):
        pass
    
def fun_two():
    print("running fun_two")
    for _ in range(1,100):
        pass
    
def fun_three():
    print("running fun_three")
    for _ in range(1,100):
        pass
        
if __name__ == "__main__":
    app = App()
    app.mainloop()