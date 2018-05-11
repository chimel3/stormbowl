import config
import classes.player
import classes.club

def create_players():
    '''
    ABOUT:
    Creates the players for the game.
    gametype tells us whether it's a single game or a league so that we can generate the right number of players.
    names set to None will allow us to randomly generate them.
    
    Need to read in a config file that has the race_lookup as well as info to randomly generate names. Probably hold this in JSON so can also say what sort of race the name is suitable for.
    
    UPDATE:
    Need to allow it to pick up hard-coded players names for clubs in the config file rather than generate random ones every time.
    Prerequisite for this function is that the clubs exist as this will also try and join the players to a club.
    
    read game for the clubs
    for each club:
        read config file to see if there are any fixed players associated with that club
        if so call the player class with these attributes fed in for the players
        make up the rest to 15 for each club with calls to player class with no parms. At present don't worry about race as only human. Will need to rethink that soon. Feels like an attribute of team as to what sort of races should be possible.
        add player to club
    '''
    
    '''
    IDEAS:
    race_lookup = {'Human': Human, 'Elf': Elf} - need to look at how this case statement replacement works. Need to read this in from a config file.
    
    players = []
    for club in clubs:
        if gametype == 'single':
            for 1 to 15:  # 15 is number of players for single game
                players.append(race_lookup[race]{parms...}
                club.add_player_to_club(players[-1])  # adds last player in list to club
                players[-1].add_player_to_club(club.name)
                
    return players
        
    '''
    print("starting create_players")
    # iterate through the clubs attribute of game object
    for club in config.game.clubs:
        # get just the team from the config file that relates to this club
        team_data = next(team for team in config.teams_data if team['name'] == club.name)
        if 'players' in team_data:
            # there are some fixed players so create these players
            for player_uuid in team_data['players']:
                # locate the matching player attributes in the config file
                player_data = next(player for player in config.players_data if player['uuid'] == player_uuid)
                # call Player class to create the new player
                player_class = 'classes.player.' + player_data['race']
                player = eval(player_class)(player_data)  # eval allows us to execute strings
                # store the player in the game
                classes.game.Game.add_player(config.game, player)
                classes.club.Club.add_player_to_club(club, player)
                
        # now need to create any random players to make up the rest of the team
        # for 15 minus len(team_data)['players']
        
        for _ in range(config.settings_data['players_per_team'] - len(team_data['players'])):
            # need a way to decide which race this player is. Hardcoded as Human currently.
            player = classes.player.Human()
            classes.game.Game.add_player(config.game, player)
            classes.club.Club.add_player_to_club(club, player)
        
        



import classes.game
