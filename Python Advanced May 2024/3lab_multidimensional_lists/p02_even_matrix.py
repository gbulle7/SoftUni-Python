# Method 1
print([[int(x) for x in input().split(', ') if int(x) % 2 == 0] for i in range(int(input()))])

# Method 2
# rows = int(input())
# matrix = []
#
# for r in range(rows):
#     row = [int(x) for x in input().split(', ')]
#     # row = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
#     matrix.append([element for element in row if element % 2 == 0])
#     # matrix.append(row)
# print(matrix)

# Method 3
# for r in range(rows):
#     row = input().split(', ')
#     matrix.append(map(int, row))
# even_matrix = [[x for x in row if x % 2 == 0] for row in matrix]
# print(even_matrix)
