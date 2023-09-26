n = int(input())

for row in range(1, n + 1):
    for col in range(row):
        print('$', end=' ')
    print()

# method 2
# count = int(input())
#
# for i in range(count):
#     print("$", end="")
#     for j in range(i):
#         print(" $", end="")
#     print()