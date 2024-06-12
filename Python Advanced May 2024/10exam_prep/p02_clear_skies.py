size = int(input())

field = []
own_jet = (0, 0)
own_jet_armor = 300
enemies = []
win = False
game_over = False

for row in range(size):
    field.append(list(input()))
    for col in range(len(field[row])):
        if field[row][col] == 'E':
            enemies.append((row, col))
        elif field[row][col] == 'J':
            own_jet = (row, col)

mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while enemies and own_jet_armor:
    command = input()
    move_r, move_c = mapper[command]
    new_r, new_c = own_jet[0] + move_r, own_jet[1] + move_c
    field[own_jet[0]][own_jet[1]] = '-'
    own_jet = (new_r, new_c)

    if field[new_r][new_c] == 'E':
        enemies.remove((new_r, new_c))
        if not enemies:
            win = True
        else:
            own_jet_armor -= 100
            if own_jet_armor <= 0:
                game_over = True

    elif field[new_r][new_c] == 'R':
        own_jet_armor = 300

    field[new_r][new_c] = 'J'

    if win:
        print(f'Mission accomplished, you neutralized the aerial threat!')
        break
    if game_over:
        print(f'Mission failed, your jetfighter was shot down! Last coordinates [{own_jet[0]}, {own_jet[1]}]!')
        break

[print(''.join(row)) for row in field]
