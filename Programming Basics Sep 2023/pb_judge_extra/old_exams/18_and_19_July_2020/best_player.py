most_goals = 0
best_player = ''
hattrick = False

while True:
    player_name = input()
    if player_name == 'END':
        break
    goals = int(input())
    if goals > most_goals:
        most_goals = goals
        best_player = player_name
    if goals >= 3:
        hattrick = True
    if goals >= 10:
        break

print(f"{best_player} is the best player!")
if hattrick:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")