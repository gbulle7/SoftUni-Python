size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
bombs = [tuple(int(x) for x in bmb.split(',')) for bmb in input().split()]


def explosion(mat, r, c):
    value = mat[r][c]
    for x_row in range(r - 1, r + 2):
        for x_col in range(c - 1, c + 2):
            if x_row in range(len(mat)) and x_col in range(len(mat[x_row])):
                if mat[x_row][x_col] > 0:
                    mat[x_row][x_col] -= value
    mat[r][c] = 0
    return mat


for bomb in bombs:
    b_row, b_col = bomb
    if matrix[b_row][b_col] > 0:
        matrix = explosion(matrix, b_row, b_col)

# alive_cells = []
# for row in matrix:
#     for col in row:
#         if col > 0:
#             alive_cells.append(col)
alive_cells = [x for row in matrix for x in row if x > 0]
print(f'Alive cells: {len(alive_cells)}')
print(f'Sum: {sum(alive_cells)}')
[print(*row) for row in matrix]
# for row in matrix:
#     print(" ".join(str(x) for x in row))
