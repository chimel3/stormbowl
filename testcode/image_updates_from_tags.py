import tkinter as tk
from math import pi, cos, sin, sqrt
import random
import sys



def click(event):
    print("5")
    currentItem = (canvas.find_withtag('current'))
    print(canvas.gettags(currentItem))
    canvas.delete("all")
    canvas.create_image(50,100,image=image2, tags=('disabled', 'fb930228-1414-4b44-a70e-546151306e20'))
    print("6")

    
'''
LOOKS AT AUTO UPDATING IMAGES DEPENDING ON TAGS ON EVENT REFRESHES
'''

import  tkinter as tk
import uuid
master = tk.Tk()
master.title("charplace")

canvas = tk.Canvas(master, 
                       width=500, 
                       height=500,
                       background='red', 
                       borderwidth=0)
    
image1 = tk.PhotoImage(file="sample.gif")
image2 = tk.PhotoImage(file="samplegrey-2.gif")

canvas.create_image(50,100,image=image1, tags=('enabled', 'fb930228-1414-4b44-a70e-546151306e20'))
print("1")
canvas.bind("<Button-1>", click)
print("2")
canvas.pack()
print("3")

master.mainloop() 
print("4")


