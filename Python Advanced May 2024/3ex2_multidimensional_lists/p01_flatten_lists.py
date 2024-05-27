line = [x.split() for x in input().split('|')]
[print(*el, end=' ') for el in line[::-1] if el]

# Method 2
# line = [[x.strip() for x in sublist.split()] for sublist in input().split('|')]
# flattened_list = []
# while line:
#     current_list = line.pop()
#     flattened_list.extend(current_list)
# print(*flattened_list)

# Method 3
# strings = input().split('|')
# matrix = []
#
# for i in range(len(strings) - 1, -1, -1):
#     row = [*strings[i].split()]  # row = strings[i].split()
#     if row:
#         matrix.append(row)
# for row in matrix:
#     print(*row, end=' ')
