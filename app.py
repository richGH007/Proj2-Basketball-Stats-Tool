from constants import TEAMS
from constants import PLAYERS

team_list = TEAMS.copy()
player_list = PLAYERS.copy()

player_list_exp = []
player_list_noob = []
player_list_ordered = []

bandits = []
bandits_guardians = []
panthers = []
panthers_guardians = []
warriors = []
warriors_guardians = []


def clean_data():
    for player in player_list:
        if (player['experience']) == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
        height, unit = player['height'].split(" ")
        player['height'] = int(height)
        if ' and ' in player['guardians']:
            guard1, guard2 = player['guardians'].split(' and ')
            player['guardians'] = guard1 + ", " + guard2
            # print('* {}'.format(player['guardians'])) # prints if two guardians


def add_to_exp_player(current_player):
    player_list_exp.append(current_player)


def add_to_noob_player(current_player):
    player_list_noob.append(current_player)


if __name__ == "__main__":

    clean_data()

    # Resorting the players so that the experienced are first
    count_exp_player = 0
    count_noob_player = 0
    for player in player_list:
        if (player['experience']):
            add_to_exp_player(player)
            count_exp_player += 1
        else:
            add_to_noob_player(player)
            count_noob_player += 1
    player_list_ordered = player_list_exp + player_list_noob
    player_list = player_list_ordered.copy()
    #print(f'player_list after copy: {player_list}')

    bandits_players = 0
    bandits_exp_players = 0
    panthers_players = 0
    panthers_exp_players = 0
    warriors_players = 0
    warriors_exp_players = 0

    bandits_total_height = 0
    panthers_total_height = 0
    warriors_total_height = 0

    for player in player_list:
        if len(bandits) <= len(panthers) and len(bandits) <= len(warriors):
            bandits.append(player['name'])
            bandits_guardians.append(player['guardians'])
            bandits_players += 1
            bandits_total_height += player['height']
            if (player['experience']):
                bandits_exp_players += 1
        elif len(panthers) <= len(bandits) and len(panthers) <= len(warriors):
            panthers.append(player['name'])
            panthers_guardians.append(player['guardians'])
            panthers_players += 1
            panthers_total_height += player['height']
            if (player['experience']):
                panthers_exp_players += 1
        elif len(warriors) <= len(bandits) and len(warriors) <= len(panthers):
            warriors.append(player['name'])
            warriors_guardians.append(player['guardians'])
            warriors_players += 1
            warriors_total_height += player['height']
            if (player['experience']):
                warriors_exp_players += 1
        else:
            print('This player {} was not added.'.format(player['name']))

    print("bandits:  {} with {} experienced".format(
        bandits, bandits_exp_players))
    print("panthers: {} with {} experienced".format(
        panthers, panthers_exp_players))
    print("warriors: {} with {} experienced".format(
        warriors, warriors_exp_players))

    print(f'Bandits_Guardians: {", ".join(bandits_guardians)}')
    print(f'Panthers_Guardians: {", ".join(panthers_guardians)}')
    print(f'Warriors_Guardians: {", ".join(warriors_guardians)}')
