# Method 1
rows, columns = [int(x) for x in input().split(', ')]
matrix = [list(map(int, input().split())) for row in range(rows)]

sums = [sum([row[i] for row in matrix]) for i in range(columns)]
print(*sums, sep='\n')
# [print(x) for x in sums]


# Method 2
sums = []
for i in range(columns):
    sums.append([])
    for row in matrix:
        sums[i].append(row[i])
print(*[sum(col) for col in sums], sep='\n')


# Method 3
# rows, columns = [int(x) for x in input().split(', ')]
# matrix = []
# for _ in range(rows):
#     row = [int(x) for x in input().split()]
#     matrix.append(row)
# result = []
# for column_index in range(columns):
#     column_sum = 0
#     for row_index in range(rows):
#         column_sum += matrix[row_index][column_index]
#     result.append(column_sum)
#     print(column_sum)

