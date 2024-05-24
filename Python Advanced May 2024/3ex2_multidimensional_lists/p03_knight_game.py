def possible_attacks(r, c, mat, s):
    result = 0
    if (r - 1) in range(s) and (c - 2) in range(s) and mat[r - 1][c - 2] == 'K':
        result += 1
    if (r - 2) in range(s) and (c - 1) in range(s) and mat[r - 2][c - 1] == 'K':
        result += 1
    if (r - 2) in range(s) and (c + 1) in range(s) and mat[r - 2][c + 1] == 'K':
        result += 1
    if (r - 1) in range(s) and (c + 2) in range(s) and mat[r - 1][c + 2] == 'K':
        result += 1
    if (r + 1) in range(s) and (c + 2) in range(s) and mat[r + 1][c + 2] == 'K':
        result += 1
    if (r + 2) in range(s) and (c + 1) in range(s) and mat[r + 2][c + 1] == 'K':
        result += 1
    if (r + 2) in range(s) and (c - 1) in range(s) and mat[r + 2][c - 1] == 'K':
        result += 1
    if (r + 1) in range(s) and (c - 2) in range(s) and mat[r + 1][c - 2] == 'K':
        result += 1

    return result


size = int(input())
matrix = [list(input()) for _ in range(size)]
removed_knights = 0
k_row, k_col = (0, 0)

while True:
    max_attacks = 0
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                attacks = possible_attacks(row, col, matrix, size)
                if attacks > max_attacks:
                    max_attacks = attacks
                    k_row, k_col = (row, col)
    if max_attacks == 0:
        break
    matrix[k_row][k_col] = '0'
    removed_knights += 1

print(removed_knights)
