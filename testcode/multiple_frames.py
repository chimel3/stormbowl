import tkinter as tk
from math import pi, cos, sin, sqrt
import random
import sys

    

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Title window")
        self.geometry("300x300")
        self.switch_frame(StartPage)
        
    def switch_frame(self, frame_class):
        '''destroy current frame and replace with new one'''
        new_frame = frame_class(self)
        if hasattr(self, "_frame"):
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
    def set_window_size(self, size):
        self.geometry(size)
        

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #master.geometry("150x150")
        App.set_window_size(master, "170x250")
        master.title("Start page")
        btn1 = tk.Button(self, text="Open window 2", command=lambda : master.switch_frame(WinTwo))
        btn2 = tk.Button(self, text="Open window 3", command=lambda : master.switch_frame(WinThree))
        btn1.pack()
        btn2.pack()
        
class WinTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #master.geometry("450x150")
        App.set_window_size(master, "350x50")
        master.title("Window 2")
        btn3 = tk.Button(self, text="Return to title page", command=lambda : master.switch_frame(StartPage))
        btn3.pack()
        
class WinThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        App.set_window_size(master, "400x400")
        #master.geometry("150x450")
        master.title("Window 3")
        btn4 = tk.Button(self, text="Return to title page", command=lambda : master.switch_frame(StartPage))
        btn4.pack()
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()