rows = int(input())
# matrix = []
# [matrix.append(list(map(int, input().split(', ')))) for row in range(rows)]
matrix = [map(int, input().split(', ')) for row in range(rows)]

print([element for row in matrix for element in row])

# flattened_matrix = []
# for row in matrix:
#     for element in row:
#         flattened_matrix.append(element)
# print(flattened_matrix)
