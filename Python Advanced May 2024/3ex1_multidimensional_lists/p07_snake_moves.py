from collections import deque

rows, columns = [int(x) for x in input().split()]
snake = deque(input())
matrix = []

for row in range(rows):
    current_row = ''
    for col in range(columns):
        current_char = snake.popleft()
        current_row += current_char
        snake.append(current_char)
    if row % 2 != 0:
        current_row = current_row[::-1]
    matrix.append(current_row)

[print(element) for element in matrix]


# Method 2
# for row in range(rows):
#     matrix.append([' '] * columns)
#     for col in range(columns):
#         if row % 2 == 0:
#             matrix[row][col] = snake[0]
#         else:
#             matrix[row][-1 - col] = snake[0]
#         snake.rotate(-1)
# [print(*row, sep='') for row in matrix]