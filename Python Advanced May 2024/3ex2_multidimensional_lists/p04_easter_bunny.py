size = int(input())
matrix = []
bunny = (0, 0)

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'B':
            bunny = (row, col)

possible_moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
max_eggs = -float('inf')
max_direction = ''
max_eggs_matrix = []

for direction, move in possible_moves.items():
    curr_eggs = 0
    curr_eggs_matrix = []
    next_r = bunny[0] + move[0]
    next_c = bunny[1] + move[1]

    while next_r in range(size) and next_c in range(size):
        if matrix[next_r][next_c] == 'X':
            break
        curr_eggs += int(matrix[next_r][next_c])
        curr_eggs_matrix.append([next_r, next_c])
        next_r += move[0]
        next_c += move[1]
    if curr_eggs > max_eggs and curr_eggs_matrix:
        max_eggs = curr_eggs
        max_direction = direction
        max_eggs_matrix = curr_eggs_matrix

print(max_direction)
[print(row) for row in max_eggs_matrix]
print(max_eggs)


# Method 2
# def best_path(r, c, mat):
#     best_direction = ''
#     eggs_positions = []
#     max_eggs = -float('inf')
#     for path in ['up', 'down', 'left', 'right']:
#         current_sum = 0
#         current_positions = []
#         if path == 'up':
#             for i in range(r - 1, -1, -1):
#                 if mat[i][c] == 'X':
#                     break
#                 current_sum += mat[i][c]
#                 current_positions.append([i, c])
#         elif path == 'down':
#             for i in range(r + 1, len(mat)):
#                 if mat[i][c] == 'X':
#                     break
#                 current_sum += mat[i][c]
#                 current_positions.append([i, c])
#         elif path == 'left':
#             for i in range(c - 1, -1, -1):
#                 if mat[r][i] == 'X':
#                     break
#                 current_sum += mat[r][i]
#                 current_positions.append([r, i])
#         elif path == 'right':
#             for i in range(c + 1, len(mat)):
#                 if mat[r][i] == 'X':
#                     break
#                 current_sum += mat[r][i]
#                 current_positions.append([r, i])
#         if current_sum > max_eggs and current_positions:
#             max_eggs = current_sum
#             eggs_positions = current_positions
#             best_direction = path
#
#     return best_direction, eggs_positions, max_eggs
#
#
# size = int(input())
# field = []
# b_row, b_col = (0, 0)
#
# for row in range(size):
#     field.append([x if x in 'XB' else int(x) for x in input().split()])
#     for col in range(size):
#         if field[row][col] == 'B':
#             b_row, b_col = row, col
#             break
#
# direction, positions, collected_eggs = best_path(b_row, b_col, field)
# print(direction)
# [print(position) for position in positions]
# print(collected_eggs)
# # [print(*row) for row in field]
