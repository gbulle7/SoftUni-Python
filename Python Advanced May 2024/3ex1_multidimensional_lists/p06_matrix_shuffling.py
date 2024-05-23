rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for x in range(rows)]

command = input()

while command != 'END':
    command = command.split()
    if command[0] != 'swap' or len(command) != 5:
        print('Invalid input!')
    else:
        row1, col1, row2, col2 = [int(x) for x in command[1:]]
        if row1 in range(rows) and col1 in range(columns) and row2 in range(rows) and col2 in range(columns):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*row) for row in matrix]
        else:
            print('Invalid input!')
    command = input()


# Method 2
# def shuffle_matrix(row1, col1, row2, col2):
#     matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#
#
# rows, columns = [int(x) for x in input().split()]
# matrix = [input().split() for x in range(rows)]
#
# while True:
#     command = input()
#     if command == "END":
#         break
#     if not command.startswith("swap") or len(command.split()) != 5:
#         print("Invalid input!")
#         continue
#     row_1, col_1, row_2, col_2 = [int(x) for x in command.split()[1:]]
#     if row_1 in range(rows) and col_1 in range(columns) and row_2 in range(rows) and col_2 in range(columns):
#         shuffle_matrix(row_1, col_1, row_2, col_2)
#         [print(" ".join(element)) for element in matrix]
#     else:
#         print("Invalid input!")
