import tkinter as tk
from math import pi, cos, sin, sqrt
import random
import sys

    

class Titlewindow(object):
    def __init__(self, parent):
        self.root = parent
        self.root.title("Title window")
        self.root.geometry("300x300")
        self.frame = tk.Frame(parent)
        self.frame.pack()
        
        btn1 = tk.Button(self.frame, text="Open Window 2", command=lambda : Windowtwo(self.root))
        btn1.pack()
        
    def hide(self):
        self.withdraw()

    def show(self):
        self.deiconify()
        
        
class Windowtwo(tk.Toplevel):
    def __init__(self, root): # root passed to allow us to pass it in hide/show
        tk.Toplevel.__init__(self)
        self.geometry("300x500")
        self.title("Window two")
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        
        btn2 = tk.Button(self.frame, text="Hide title window", command=lambda : Titlewindow.hide(root))
        btn2.pack()
        
        btn3 = tk.Button(self.frame, text="Show title window", command=lambda : Titlewindow.show(root))
        btn3.pack()
        
        #self.show(self)
        
    def hide(self):
        self.withdraw()
        
    def show(self):
        self.deiconify()

        
        
root = tk.Tk()
app = Titlewindow(root)
root.mainloop()