# Function to find the starting position of the jetfighter ('J') in the airspace
def find_start_position(size, airspace):
    for i in range(size):
        for j in range(size):
            if airspace[i][j] == 'J':
                return [i, j]
    return None


# Function to handle the effects of the jetfighter's current position
def handle_current_position(position, airspace, armor, enemy_planes):
    current_char = airspace[position[0]][position[1]]

    if current_char == 'E':
        if enemy_planes != 1:
            armor -= 100
        enemy_planes -= 1
    elif current_char == 'R':
        if armor < 300:
            armor = 300

    airspace[position[0]][position[1]] = 'J'

    return armor, enemy_planes


# Function to move the jetfighter based on the given command
def move_plane(command, position, airspace):
    row, col = position

    airspace[row][col] = '-'

    if command == "up":
        position[0] -= 1
    elif command == "down":
        position[0] += 1
    elif command == "left":
        position[1] -= 1
    elif command == "right":
        position[1] += 1

    return position


# Function to print the final state of the matrix (airspace)
def print_final_state(airspace):
    for row in airspace:
        print(''.join(row))


# Main function to simulate the jetfighter scenario
def clear_skies():
    armor = 300
    enemy_planes = 4

    size = int(input())
    airspace = [list(input()) for _ in range(size)]

    current_position = find_start_position(size, airspace)

    while True:
        if armor <= 0:
            assert current_position is not None
            print(
                f"Mission failed, your jetfighter was shot down! Last coordinates [{current_position[0]}, {current_position[1]}]!")
            break

        if enemy_planes == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break

        command = input()
        assert current_position is not None
        move_plane(command, current_position, airspace)
        armor, enemy_planes = handle_current_position(current_position, airspace, armor, enemy_planes)

    print_final_state(airspace)


clear_skies()
