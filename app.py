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
    print(f'player_list_ordered: {player_list_ordered}')
