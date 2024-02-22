team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

card = input().split()
terminated = False

for player in card:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        terminated = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if terminated:
    print('Game was terminated')


# card = input()
# combined = card.split()
# combined = set(combined)
# combined = list(combined)
#
# a_team = []
# b_team = []
# terminated = True
#
# while combined:
#     pop = combined.pop()
#     if 'A' in pop:
#         a_team.append(pop)
#         if len(a_team) >= 5:
#             break
#     elif 'B' in pop:
#         b_team.append(pop)
#         if len(b_team) >= 5:
#             break
# else:
#     terminated = False
#
# players_a = 11 - len(a_team)
# players_b = 11 - len(b_team)
#
# print(f'Team A - {players_a}; Team B - {players_b}')
# if terminated:
#     print('Game was terminated')
