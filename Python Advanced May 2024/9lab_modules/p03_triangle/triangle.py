# def print_triangle(size):
#     for row in range(size):
#         for col in range(1, row + 2):
#             print(col, end=' ')
#         print()
#
#     for row in range(size - 1, 0, -1):
#         for col in range(1, row + 1):
#             print(col, end=' ')
#         print()


def print_triangle(size):
    for row in range(2, size + 2):
        print(*[col for col in range(1, row)])
    for row in range(size, 0, -1):
        print(*[col for col in range(1, row)])
