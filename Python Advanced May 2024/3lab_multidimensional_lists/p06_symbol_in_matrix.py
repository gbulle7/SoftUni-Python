# Method 1
size = int(input())
matrix = [[x for x in input()] for i in range(size)]
symbol = input()
for row in matrix:
    if symbol in row:
        print((matrix.index(row), row.index(symbol)))
        break
else:
    print(f'{symbol} does not occur in the matrix')

# Method 2
# size = int(input())
# matrix = []
# for _ in range(size):
#     matrix.append(list(input()))
# symbol = input()
# location = None
# for row in range(size):
#     if location:
#         break
#     for col in range(size):
#         if matrix[row][col] == symbol:
#             location = (row, col)
#             break
# if location:
#     print(location)
# else:
#     print(f"{symbol} does not occur in the matrix")
