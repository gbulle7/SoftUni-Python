rows, columns = [int(x) for x in input().split()]
matrix = [['' for elements in range(columns)] for row in range(rows)]
i = ord('a')

for r in range(rows):
    curr_row = []
    for c in range(columns):
        matrix[r][c] = f'{chr(i + r) + chr(i + r + c) + chr(i + r)}'

[print(*row) for row in matrix]


# Method 2
# matrix = []
# for row in range(rows):
#     current_row = []
#     for col in range(columns):
#         first_letter = chr(97 + row)
#         second_letter = chr(97 + row + col)
#         third_letter = first_letter
#         palindrome = first_letter + second_letter + third_letter
#         current_row.append(palindrome)
#     matrix.append(current_row)

# Method 3
# rows, columns = [int(x) for x in input().split()]
# i = ord('a')
# for row in range(rows):
#     for col in range(columns):
#         print(f'{chr(i + row)}{chr(i + row + col)}{chr(i + row)}', end=' ')
#     print()
