import tkinter as tk
from math import pi, cos, sin, sqrt
import random
import sys


class Man(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_older(self):
        self.age += 1
        
        
class Team(object):
    def __init__(self, name):
        self.name = name
        self.players = []
        
    def add_player(self, player):
        self.players.append(player)
        
    def age_player(self, player):
        self.players[0].age += 1
        
        

'''
SHOWS HOW TO DYNAMICALLY LOOKUP A CLASS AND THAT OBJECTS ARE PASSED BY REF
'''
class_lookup = {'Team': Team, 'Man': Man}
team1 = class_lookup['Team']("Rovers")
man1 = class_lookup['Man']("tim", 28)
#man1 = Man("tim", 28)
team1.add_player(man1)
print(team1.players)
print("original player age: " + str(team1.players[0].age))
# man1.get_older()
team1.age_player(man1)
print("new player age man object: " + str(man1.age))
print("new player age team object: " + str(team1.players[0].age))

# this proves that the object is passed as a reference and so if you update the object itself it is updated in teams too


