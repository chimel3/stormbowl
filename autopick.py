import config

def autopick_players(club):
    player_abilities = []    # create a list to hold a sum of each player's numeric abilities
    for player in club.players:
        if player.availability == 'available':
            player_abilities.append([player.uuid, sum([player.movement, 
                                                     player.attack,
                                                     player.defense,
                                                     player.toughness,
                                                     player.resilience,
                                                     player.throwing,
                                                     player.kicking,
                                                     player.agility,
                                                     player.catching])])

    player_abilities.sort(key=lambda x : x[1], reverse=True)  # sort by highest sum of abilities
    
    # set the number of players in the squad and team
    if len(player_abilities) < 15:
        num_in_squad = len(player_abilities)
        if len(player_abilities) < 11:
            num_in_team = len(player_abilities)
        else:
            num_in_team = 11
    else:
        num_in_squad = 15
        num_in_team = 11
    
    # pick team        
    for row in range(0,num_in_team):
        picked_player = next(player for player in config.game.players if player.uuid == player_abilities[row][0])
        picked_player.playingstatus = "team"
        
    # pick squad
    for row in range(num_in_team,num_in_squad):
        picked_player = next(player for player in config.game.players if player.uuid == player_abilities[row][0])
        picked_player.playingstatus = "squad"        
