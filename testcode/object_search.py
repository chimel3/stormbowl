class Club(object):
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager
        

clublist = []
club1 = Club("ClubA", "computer")
print(type(club1))
club2 = Club("ClubB", "computer")
clublist.append([club1, club2])

club1 = Club("ClubC", "computer")
club2 = "computer"
clublist.append([club1, club2])

club1 = Club("ClubE", "dayoff")
club2 = Club("ClubD", "human")
clublist.append([club1, club2])

#answer = next(x for x in clublist if x[0].manager == "human" or x[1].manager == "human")
#print(answer[0].name + " v " + answer[1].name)
#print(clublist.index(next(x for x in clublist if x[0].manager == "human" or x[1].manager == "human")))

# following line basically searches within each 'row', or 'y', and then within each item in the 'x' list, or 'y'.
#print(clublist.index(next(y for y in clublist if [x for x in y if x.manager == "human"])))
print(clublist.index(next(y for y in clublist if [x for x in y if not isinstance(x, str) if x.manager == "human"])))

'''
Remove the element containing the human player and add it to the end of the list
Breaking this line up to understand it:

[x for x in y if not isinstance(x, str) if x.manager == "human"] - list comprehension with 2 if conditions, the first checks that x is not a string ("dayoff" is a string), and then if it's not it will check whether the name property equals "human". y is passed from earlier in the line.

next(y for y in clublist if - this finds the first match - next - in the rows of the list - y.

clublist.index() - this will find the index position in the list of the value in the ()

clublist.pop() - removes the element in the list that we've found that satisfies the above conditions.

clublist.append() - adds the removed element to the end of the list.
'''

clublist.append(clublist.pop(clublist.index(next(y for y in clublist if [x for x in y if not isinstance(x, str) if x.manager == "human"]))))

for fixture in clublist:
    if isinstance(fixture[0], str):
        print(fixture[0] + " v " + fixture[1].name)
    elif isinstance(fixture[1], str):
        print(fixture[0].name + " v " + fixture[1])
    else:
        print(fixture[0].name + " v " + fixture[1].name)
        
fix = (club1, club2)
if [x for x in fix if not isinstance(x, str) if x.manager == "human"]:
    print("yep")
else:
    print("nope")
    
#clublist.append(answer, )


#team_data = next(team for team in config.teams_data if team['name'] == club.name)
#        if 'players' in team_data: