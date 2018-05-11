import config
import random

def create_fixture_list():
    '''
    ABOUT:
    Uses the circle algorithm to produce a round-robin style fixture list.
    
    '''
    '''
    IDEAS:
    
    '''
    print("starting create_fixture_list")
    # Create a new list to hold the clubs. Whilst I could just use the list of clubs held in the game, this wouldn't work where the total number of clubs is an odd number as I then have to create a "DayOff" club.
    clublist = config.game.clubs
    if len(clublist) % 2:
        clublist.append("DayOff")
        
    # set the number of fixtures per round
    classes.game.Game.fixtures_per_round(config.game, int(len(clublist)/2)) # this is cast to an int because otherwise it automatically becomes a float and the for loop in get_fixtures_for_round fails
        
    # shuffle clublist to get some randomness in there to the schedule.
    random.shuffle(clublist)
    
    # create the fixture list variables
    #config.start_fixture_list()
        
    for week in range(1, len(clublist)):
        for i in range(int(len(clublist)/2)):    # for the number of matches
            
            # attempt to keep a mixture of home and away games
            if week % 2:
                #config.fixtures.append((clublist[i], clublist[len(clublist)-1-i]))
                classes.game.Game.add_fixture(config.game, clublist[i], clublist[len(clublist)-1-i])
                #config.returnfixtures.append((clublist[len(clublist)-1-i], clublist[i]))
                classes.game.Game.add_returnfixture(config.game, clublist[len(clublist)-1-i], clublist[i])
            else:
                #config.fixtures.append((clublist[len(clublist)-1-i], clublist[i]))
                classes.game.Game.add_fixture(config.game, clublist[len(clublist)-1-i], clublist[i])
                #config.returnfixtures.append((clublist[i], clublist[len(clublist)-1-i] ))
                classes.game.Game.add_returnfixture(config.game, clublist[i], clublist[len(clublist)-1-i])
                
        # move the last club up to the 2nd position in the list
        clublist.insert(1, clublist.pop())
        
    #return len(clublist-1)  # number of rounds is the number of clubs in the draw (includes DayOff) minus 1.

    '''
    # following code is troubleshooting code to show the fixtures in full
    for fixture in config.fixtures:
        if isinstance(fixture[0], str):
            print(fixture[0] + " v " + fixture[1].name)
        elif isinstance(fixture[1], str):
            print(fixture[0].name + " v " + fixture[1])
        else:
            print(fixture[0].name + " v " + fixture[1].name)
    '''
    
import classes.game       
