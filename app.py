from constants import TEAMS
from constants import PLAYERS

team_list = TEAMS.copy()
player_list = PLAYERS.copy()

bandits = []
bandits_guardians = []
panthers = []
panthers_guardians = []
warriors = []
warriors_guardians = []

print()
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
print()

for player in player_list:
    if len(bandits) <= len(panthers) and len(bandits) <= len(warriors):
        bandits.append(player['name'])
        bandits_guardians.append(player['guardians'])
    elif len(panthers) <= len(bandits) and len(panthers) <= len(warriors):
        panthers.append(player['name'])
        panthers_guardians.append(player['guardians'])
    elif len(warriors) <= len(bandits) and len(warriors) <= len(panthers):
        warriors.append(player['name'])
        warriors_guardians.append(player['guardians'])
    else:
        print('This player {} was not added.'.format(player['name']))

# print("bandits:  {}".format(bandits))  # prints bandits list
# print("bandits_guardians:  {}".format(bandits_guardians)) # prints bandits_guardians list
# print()
# print("panthers: {}".format(panthers)) # prints panthers list
# print("panthers_guardians: {}".format(panthers_guardians)) # prints panthers_guardians list
# print()
# print("warriors: {}".format(warriors)) # prints warriors list
# print("warriors_guardians: {}".format(warriors_guardians)) # prints warriors_guardians list
# print()
print(f'Bandits: {", ".join(bandits)}')
print(f'Bandits_Guardians: {", ".join(bandits_guardians)}')
print()
print(f'Panthers: {", ".join(panthers)}')
print(f'Panthers_Guardians: {", ".join(panthers_guardians)}')
print()
print(f'Warriors: {", ".join(warriors)}')
print(f'Warriors_Guardians: {", ".join(warriors_guardians)}')

print()
print()
print()
