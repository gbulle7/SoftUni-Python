rows, columns = [int(x) for x in input().split(', ')]
matrix = [list(map(int, input().split(', '))) for row in range(rows)]
max_sum = 0
square = [[0, 0], [0, 0]]

for row in range(rows - 1):
    for col in range(columns - 1):
        top_left = matrix[row][col]
        top_right = matrix[row][col + 1]
        bottom_left = matrix[row + 1][col]
        bottom_right = matrix[row + 1][col + 1]
        current_sum = top_left + top_right + bottom_left + bottom_right
        if current_sum > max_sum:
            max_sum = current_sum
            square[0][0] = top_left
            square[0][1] = top_right
            square[1][0] = bottom_left
            square[1][1] = bottom_right
[print(*element) for element in [row for row in square]]
print(max_sum)
