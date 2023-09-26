n = int(input())
for row in range(n):
    for col in range(n):
        print('*', end=' ')
    print('')

# method 2
# count = int(input())
#
# for i in range(count):
#     print("*", end="")
#     for j in range(count - 1):
#         print(" *", end="")
#     print()