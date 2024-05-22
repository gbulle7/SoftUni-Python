rows, columns = input().split(', ')
matrix = []

for r in range(int(rows)):
    row = list(map(int, input().split(', ')))
    matrix.append(row)
print(sum([sum(row) for row in matrix]))
print(matrix)

# Slow method
# rows, columns = [int(x) for x in input().split(', ')]
# matrix = []
# for r in range(rows):
#     matrix.append([])
#     row = list(map(int, input().split(', ')))
#     for c in range(columns):
#         matrix[r].append(row[c])
