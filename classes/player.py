from abc import ABCMeta, abstractmethod
import config
import uuid
import random

class Player(object):
    '''
    ABOUT:
    Defines a general character. They will ultimately always be of a certain type though.
    '''
    '''
    IDEAS:
    Need to work out how I have a generic Player class and child classes for the different races.
    Suggest I'll keep all of the child classes in here as well.
    See Jeff Knuff - Python Classes and Object Oriented Programming
    '''
    __metaclass__ = ABCMeta
    
    #Player state attributes
    playingstatus = None
    state = None
    availability = 'available'
    recoverytime = 0
    experience = 0
    
    #Player pictures
    image_front_active = None
    image_front_active_with_ball = None
    image_front_disabled = None
    image_front_disabled_with_ball = None
    image_back_active = None
    image_back_active_with_ball = None
    image_back_disabled = None
    image_back_disabled_with_ball = None
    
    #Player abilities
    movement = 0
    attack = 0
    defense = 0
    strength = 0
    toughness = 0
    resilience = 0
    throwing = 0
    kicking = 0
    agility = 0
    catching = 0

    
    def __init__(self, attributes=None):
        '''
        self.race = race
        if name == None:
            call random name generator method
        
        
        if attributes != None:
            print(attributes.keys())
    
        '''
    
    @abstractmethod
    def player_race(self):
        '''
        Return a string representing the race of player this is.
        '''
        pass

    
class Human(Player):

    #Default human state attributes
    race = 'Human'   # needs to start with capital letter to match the class name
    playingstatus = None
    state = None
    availability = 'available'
    recoverytime = 0
    experience = 0
    
    #Default human pictures
    image_front_active = None
    image_front_active_with_ball = None
    image_front_disabled = None
    image_front_disabled_with_ball = None
    image_back_active = None
    image_back_active_with_ball = None
    image_back_disabled = None
    image_back_disabled_with_ball = None
    
    #Default human abilities
    movement = 4
    attack = 9
    defense = 9
    strength = 8
    toughness = 8
    resilience = 5
    throwing = 10
    kicking = 10
    agility = 8
    catching = 10

    
    def __init__(self, attributes=None):
        self.race = self.player_race()
        print("starting Human initialisation")
        if attributes != None:
            for attribute in attributes.keys():
                setattr(self, attribute, attributes[attribute])
        else:
            # no attributes passed so generate the non-default ones
            self.uuid = uuid.uuid4()
            self.name = random.choice(config.firstname_data) + " " + random.choice(config.lastname_data)
            
        super().__init__(self)
        
    
    def player_race(self):
        '''Return a string representing the race of player this is'''
        return 'human'
    
    
    def change_team_colours(self, colour):
        '''
        ABOUT:
        Allows you to change the images to ones in different colours to represent the team they've joined.
        '''
        pass
        

            