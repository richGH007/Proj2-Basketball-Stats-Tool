import copy
import constants

team_list = copy.deepcopy(constants.TEAMS)
player_list = copy.deepcopy(constants.PLAYERS)

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

    view_stats = True

    while view_stats:
        print('----MENU----')
        print()
        print('Here are your choices:')
        print('A) Display Team Stats')
        print('B) Quit')
        print()
        display = (input("Enter an Option: "))
        if display.upper() == 'A' or display.upper() == "B":
            if display.upper() == 'A':
                option = True
                while option:
                    print()
                    print('A) Bandits')
                    print('B) Panthers')
                    print('C) Warriors')
                    print()
                    team_chose = (input("Enter an option: "))
                    print()
                    print()
                    print()
                    if team_chose.upper() == 'A' or team_chose.upper() == 'B' or team_chose.upper() == 'C':
                        if team_chose.upper() == 'A':
                            print('Team:  Bandits Stats')
                            print('-' * 90)
                            print(
                                f'Total players: {bandits_players}   Experienced: {bandits_exp_players}   Inexperienced: {bandits_players - bandits_exp_players}   Average Height: {round(bandits_total_height/bandits_players, 1)}-inches')
                            print()
                            print(f'Players on Team: \n {", ".join(bandits)}')
                            print()
                            print(
                                f'Bandits_Guardians: \n {", ".join(bandits_guardians)}')
                            print('-' * 90)
                            print()
                            print()
                            option = False
                        if team_chose.upper() == 'B':
                            print('Team:  Panthers Stats')
                            print('-' * 90)
                            print(
                                f'Total players: {panthers_players}   Experienced: {panthers_exp_players}   Inexperienced: {panthers_players - panthers_exp_players}   Average Height: {round(panthers_total_height/panthers_players, 1)}-inches')
                            print()
                            print(f'Players on Team: \n {", ".join(panthers)}')
                            print()
                            print(
                                f'Panthers_Guardians: \n {", ".join(panthers_guardians)}')
                            print('-' * 90)
                            print()
                            print()
                            option = False
                        if team_chose.upper() == 'C':
                            print('Team:  Warriors Stats')
                            print('-' * 90)
                            print(
                                f'Total players: {warriors_players}   Experienced: {warriors_exp_players}   Inexperienced: {warriors_players - warriors_exp_players}   Average Height: {round(warriors_total_height/warriors_players, 1)}-inches')
                            print()
                            print(f'Players on Team: \n {", ".join(warriors)}')
                            print()
                            print(
                                f'Warriors_Guardians: \n {", ".join(warriors_guardians)}')
                            print('-' * 90)
                            print()
                            print()
                            option = False
                    else:
                        option = True

                view_stats = True
            else:
                view_stats = False
        else:
            view_stats = True


print()
print('Exiting Team Stats Tool')
print()
