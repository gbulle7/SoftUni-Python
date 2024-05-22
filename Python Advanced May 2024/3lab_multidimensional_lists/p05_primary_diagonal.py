# Method 1
size = int(input())
matrix = [[int(x) for x in input().split()] for i in range(size)]
print(sum([matrix[i][i] for i in range(size)]))
# matrix = [[int(x[i]) for x in (''.join(input().split())).split()] for i in range(size)]
# print(sum([row[0] for row in matrix]))

# Method 2
sum_diagonal = 0
for i in range(size):
    sum_diagonal += matrix[i][i]
print(sum_diagonal)


# Long Method 3
# size = int(input())
# matrix = [[0] * size for row in range(size)]
# for x in range(size):
#     line = list(map(int, input().split()))
#     for y in range(size):
#         matrix[x][y] = line[y]
# sum_diagonal = sum(matrix[size - i - 1][size - i - 1] for i in range(size))
# print(sum_diagonal)
