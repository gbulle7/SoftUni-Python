from sys import maxsize

rows, columns = [int(x) for x in input().split()]
matrix = [list(map(int, input().split())) for row in range(rows)]
max_sum = -maxsize  # max_sum = -float('inf')
sub_matrix = None

for row in range(rows - 2):
    for col in range(columns - 2):
        top_left = matrix[row][col]
        top_mid = matrix[row][col + 1]
        top_right = matrix[row][col + 2]
        mid_left = matrix[row + 1][col]
        mid_mid = matrix[row + 1][col + 1]
        mid_right = matrix[row + 1][col + 2]
        bottom_left = matrix[row + 2][col]
        bottom_mid = matrix[row + 2][col + 1]
        bottom_right = matrix[row + 2][col + 2]
        current_sum = (top_left + top_mid + top_right +
                       mid_left + mid_mid + mid_right +
                       bottom_left + bottom_mid + bottom_right)
        if current_sum >= max_sum:
            max_sum = current_sum
            sub_matrix = [
                [top_left, top_mid, top_right],
                [mid_left, mid_mid, mid_right],
                [bottom_left, bottom_mid, bottom_right]
            ]

if sub_matrix:
    print('Sum =', max_sum)
    [print(*element) for element in [row for row in sub_matrix]]
    # [print(*row) for row in sub_matrix]

# Method 2
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split()])
#
# for row in range(rows - 2):
#     for col in range(columns - 2):
#         submatrix = [
#             [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
#             [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
#             [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
#         ]
#         sum_elements = sum(submatrix[0]) + sum(submatrix[1]) + sum(submatrix[2])
#         if sum_elements > max_sum:
#             max_sum = sum_elements
#             max_submatrix = submatrix
#
# print(f"Sum = {max_sum}")
# for row in max_submatrix:
#     print(" ".join(str(x) for x in row))


# Method 3 - applicable for any size of sub matrix (just choose range of r and c)
# max_row = 0
# max_col = 0
# for row in range(rows - 2):
#     for col in range(columns - 2):
#         current_sum = 0
#         for r in range(row, row + 3):
#             for c in range(col, col + 3):
#                 current_sum += matrix[r][c]
#         if current_sum > max_sum:
#             max_sum = current_sum
#             max_row = row
#             max_col = col
# print(f'Sum = {max_sum}')
# max_submatrix = [matrix[r][max_col: max_col + 3] for r in range(max_row, max_row + 3)]
# [print(*row) for row in max_submatrix]