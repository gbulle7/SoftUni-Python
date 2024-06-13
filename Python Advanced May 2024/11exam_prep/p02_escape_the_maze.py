size = int(input())

maze = []
own_psn = (0, 0)
health = 100

won = False
defeated = False

for row in range(size):
    maze.append(list(input()))
    for col in range(len(maze[row])):
        if maze[row][col] == 'P':
            own_psn = (row, col)

mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


def check_psn(matrix, r, c):
    try:
        valid_index = matrix[r][c]
        return True
    except IndexError:
        return False


while not won and not defeated:
    command = input()
    move_r, move_c = mapper[command]
    new_r, new_c = own_psn[0] + move_r, own_psn[1] + move_c
    # if not (0 <= own_psn[0] + mapper[command][0] < size and 0 <= own_psn[1] + mapper[command][1] < size):
    #     continue
    isValid = check_psn(maze, new_r, new_c)
    if not isValid:
        continue

    if maze[new_r][new_c] == 'M':
        health -= 40
        if health <= 0:
            health = 0
            defeated = True

    elif maze[new_r][new_c] == 'H':
        health += 15
        # health = min(100, health + 15)
        if health > 100:
            health = 100
    elif maze[new_r][new_c] == 'X':
        won = True

    maze[own_psn[0]][own_psn[1]] = '-'
    own_psn = (new_r, new_c)
    maze[own_psn[0]][own_psn[1]] = 'P'

if won:
    print(f'Player escaped the maze. Danger passed!')
elif defeated:
    print(f'Player is dead. Maze over!')

print(f"Player's health: {health} units")
[print(''.join(row)) for row in maze]
