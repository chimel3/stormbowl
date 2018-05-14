import operator
class Player(object):
    def __init__(self, attributes=None):
        if attributes != None:
            for attribute in attributes.keys():
                setattr(self, attribute, attributes[attribute])
        else:
            pass
        

Tim = Player({"name": "Tim", "movement": 4, "attack": 9, "defense": 10, "resilience": 5, "status": None})
John = Player({"name": "John", "movement": 4, "attack": 10, "defense": 8, "resilience": 4, "status": None})
Alan = Player({"name": "Alan", "movement": 3, "attack": 8, "defense": 6, "resilience": 3, "status": None})
Hugo = Player({"name": "Hugo", "movement": 5, "attack": 11, "defense": 12, "resilience": 6, "status": None})
Lou = Player({"name": "Lou", "movement": 4, "attack": 9, "defense": 10, "resilience": 4, "status": None})
Rex = Player({"name": "Rex", "movement": 4, "attack": 9, "defense": 10, "resilience": 4, "status": None})
Dan = Player({"name": "Dan", "movement": 4, "attack": 9, "defense": 10, "resilience": 4, "status": None})

Players = []
Players.extend([Tim, John, Alan, Hugo, Lou, Rex, Dan])
Selector = []
for player in Players:
    Selector.append([player.name, sum([player.movement, player.attack, player.defense, player.resilience])])
    
#print(Selector)
    
Selector.sort(key=lambda x : x[1], reverse=True)
#print(Selector)
for index in range(0,4):
    eval(Selector[index][0]).status = "squad"
    
print(Tim.status)
    


