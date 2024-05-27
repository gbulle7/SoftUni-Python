size = int(input())
matrix = []
knights = []

for row in range(size):
    matrix.append(list(input()))    # matrix.append([x for x in input()])
    for col in range(size):
        if matrix[row][col] == 'K':
            knights.append([row, col])

removed_knights = 0
possible_moves = [(2, 1), (1, 2), (-1, -2), (-2, -1), (-1, 2), (2, -1), (-2, 1), (1, -2)]

while True:
    max_hits = 0
    max_knight = [0, 0]
    for k_row, k_col in knights:
        hits = 0
        for move in possible_moves:
            next_k_row = k_row + move[0]
            next_k_col = k_col + move[1]
            if next_k_row in range(size) and next_k_col in range(size):
                if matrix[next_k_row][next_k_col] == 'K':
                    hits += 1
        if hits > max_hits:
            max_hits = hits
            max_knight = [k_row, k_col]
    if max_hits == 0:
        break
    knights.remove(max_knight)
    removed_knights += 1
    matrix[max_knight[0]][max_knight[1]] = '0'
print(removed_knights)


# Method 2
# def possible_attacks(r, c, mat, s):
#     result = 0
#     if (r - 1) in range(s) and (c - 2) in range(s) and mat[r - 1][c - 2] == 'K':
#         result += 1
#     if (r - 2) in range(s) and (c - 1) in range(s) and mat[r - 2][c - 1] == 'K':
#         result += 1
#     if (r - 2) in range(s) and (c + 1) in range(s) and mat[r - 2][c + 1] == 'K':
#         result += 1
#     if (r - 1) in range(s) and (c + 2) in range(s) and mat[r - 1][c + 2] == 'K':
#         result += 1
#     if (r + 1) in range(s) and (c + 2) in range(s) and mat[r + 1][c + 2] == 'K':
#         result += 1
#     if (r + 2) in range(s) and (c + 1) in range(s) and mat[r + 2][c + 1] == 'K':
#         result += 1
#     if (r + 2) in range(s) and (c - 1) in range(s) and mat[r + 2][c - 1] == 'K':
#         result += 1
#     if (r + 1) in range(s) and (c - 2) in range(s) and mat[r + 1][c - 2] == 'K':
#         result += 1
#
#     return result
#
#
# size = int(input())
# matrix = [list(input()) for _ in range(size)]
# removed_knights = 0
# k_row, k_col = (0, 0)
#
# while True:
#     max_attacks = 0
#     for row in range(size):
#         for col in range(size):
#             if matrix[row][col] == 'K':
#                 attacks = possible_attacks(row, col, matrix, size)
#                 if attacks > max_attacks:
#                     max_attacks = attacks
#                     k_row, k_col = (row, col)
#     if max_attacks == 0:
#         break
#     matrix[k_row][k_col] = '0'
#     removed_knights += 1
#
# print(removed_knights)
