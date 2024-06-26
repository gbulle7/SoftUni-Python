presents = int(input())
size = int(input())

matrix = []
santa = []
nice_kids = 0
nice_kids_gifted = 0

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'S':
            santa = [row, col]
        elif matrix[row][col] == 'V':
            nice_kids += 1

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while presents:
    command = input()
    if command == 'Christmas morning':
        break

    r, c = santa[0] + directions[command][0], santa[1] + directions[command][1]
    if r in range(size) and c in range(size):
        if matrix[r][c] == 'V':
            presents -= 1
            nice_kids_gifted += 1
            matrix[r][c] = '-'
        elif matrix[r][c] == 'C':
            for direction in directions.values():
                next_r, next_c = r + direction[0], c + direction[1]
                if matrix[next_r][next_c] in ['V', 'X'] and presents:
                    presents -= 1
                    if matrix[next_r][next_c] == 'V':
                        nice_kids_gifted += 1
                    matrix[next_r][next_c] = '-'
        matrix[santa[0]][santa[1]] = '-'
        santa = [r, c]
        matrix[r][c] = 'S'

if presents < 1 and nice_kids - nice_kids_gifted > 0:
    print(f'Santa ran out of presents!')
for line in matrix:
    print(*line)
if nice_kids - nice_kids_gifted > 0:
    print(f'No presents for {nice_kids - nice_kids_gifted} nice kid/s.')
else:
    print(f'Good job, Santa! {nice_kids_gifted} happy nice kid/s.')


# Method 2
# presents = int(input())
# size = int(input())
# matrix = []
# s_row, s_col = 0, 0
# nice_kids = 0
# happy_nice_kids = 0
#
# for row in range(size):
#     matrix.append(input().split())
#     for col in range(size):
#         if matrix[row][col] == 'S':
#             s_row, s_col = row, col
#         elif matrix[row][col] == 'V':
#             nice_kids += 1
#
# moves = {
#     'up': lambda r, c: (r - 1, c),
#     'down': lambda r, c: (r + 1, c),
#     'left': lambda r, c: (r, c - 1),
#     'right': lambda r, c: (r, c + 1)
# }
#
# while presents:
#     command = input()
#     if command == 'Christmas morning':
#         break
#     new_s_row, new_s_col = moves[command](s_row, s_col)
#     if new_s_row in range(size) and new_s_col in range(size):
#         matrix[s_row][s_col] = '-'
#         s_row, s_col = new_s_row, new_s_col
#     if matrix[s_row][s_col] == 'V':
#         nice_kids -= 1
#         presents -= 1
#         happy_nice_kids += 1
#     elif matrix[s_row][s_col] == 'C':
#         surrounding_houses = [
#             [s_row - 1, s_col],
#             [s_row + 1, s_col],
#             [s_row, s_col - 1],
#             [s_row, s_col + 1]
#         ]
#         for h in surrounding_houses:
#             if presents == 0:
#                 break
#             h_row, h_col = h
#             if matrix[h_row][h_col] == 'X':
#                 presents -= 1
#             elif matrix[h_row][h_col] == 'V':
#                 presents -= 1
#                 nice_kids -= 1
#                 happy_nice_kids += 1
#             matrix[h_row][h_col] = '-'
#     matrix[s_row][s_col] = 'S'
#
# if not presents and nice_kids:
#     print(f'Santa ran out of presents!')
# [print(*row) for row in matrix]
# if not nice_kids:
#     print(f'Good job, Santa! {happy_nice_kids} happy nice kid/s.')
# else:
#     print(f'No presents for {nice_kids} nice kid/s.')
