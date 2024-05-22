# Method 1
rows = int(input())
matrix = []

for r in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append([element for element in row if element % 2 == 0])
print(matrix)

# Method 2
# for r in range(rows):
#     row = input().split(', ')
#     matrix.append(map(int, row))
# even_matrix = [[x for x in row if x % 2 == 0] for row in matrix]
# print(even_matrix)
