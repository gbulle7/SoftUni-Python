def best_path(r, c, mat):
    best_direction = ''
    eggs_positions = []
    max_eggs = 0
    for path in ['up', 'down', 'left', 'right']:
        current_sum = 0
        current_positions = []
        if path == 'up':
            for i in range(r - 1, -1, -1):
                if mat[i][c] == 'X':
                    break
                current_sum += mat[i][c]
                current_positions.append([i, c])
        elif path == 'down':
            for i in range(r + 1, len(mat)):
                if mat[i][c] == 'X':
                    break
                current_sum += mat[i][c]
                current_positions.append([i, c])
        elif path == 'left':
            for i in range(c - 1, -1, -1):
                if mat[r][i] == 'X':
                    break
                current_sum += mat[r][i]
                current_positions.append([r, i])
        elif path == 'right':
            for i in range(c + 1, len(mat)):
                if mat[r][i] == 'X':
                    break
                current_sum += mat[r][i]
                current_positions.append([r, i])
        if current_sum >= max_eggs:
            max_eggs = current_sum
            eggs_positions = current_positions
            best_direction = path

    return best_direction, eggs_positions, max_eggs


size = int(input())
field = []
b_row, b_col = (0, 0)

for row in range(size):
    field.append([x if x in 'XB' else int(x) for x in input().split()])
    for col in range(size):
        if field[row][col] == 'B':
            b_row, b_col = row, col
            break

direction, positions, collected_eggs = best_path(b_row, b_col, field)
print(direction)
[print(position) for position in positions]
print(collected_eggs)
[print(*row) for row in field]
