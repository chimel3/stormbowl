class Club(object):
    '''
    ABOUT:
    Creates a club object. Can provide default values or specify them.
    '''

    def __init__(self, name, manager, pitchsize=(24,12)):
        '''Could have human name but can always implement later if need it'''
        self.name = name
        self.players = []
        self.pitchsize = pitchsize  # this is a future development to allow different sized pitches.
        self.manager = manager   # either human or computer.

    def add_player_to_club(self, player):
        '''
        IDEAS:
        self.players.append(player)
        '''
        self.players.append(player)
    
    def change_pitch_size(self, new_size=None):
        '''
        ABOUT:
        This is called after the class contructor by the calling program if it wants to create some variability in the size of the pitches between clubs.
        '''
        '''
        IDEAS:
        If none for new_size then random or a tuple containing the size or do these different types stop me?
        if new_size == "random":
            create random pitch size within some bounds
        '''
        pass
        
