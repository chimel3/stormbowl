
class Boardspace(object):
    def __init__(self, position):
        self.position = position
        
class Hex(Boardspace):
    def __init__(self, size, position):
        self.size = size
        super().__init__(position)
        
        
space = Boardspace(4)
print("space: " + str(space.position))

hex = Hex(15, 4)
print("hex: " + str(hex.position) + "  " + str(hex.size))
        