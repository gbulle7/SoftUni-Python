number = int(input())

for row_up in range(1, number + 1):
    print(" " * (number - row_up), end="")
    print("*", end="")
    for star1 in range(row_up - 1):
        print(" *", end="")
    print()

for row_down in range(number - 1, 0, -1):
    print(" " * (number - row_down), end="")
    print("*", end="")
    for star2 in range(row_down - 1):
        print(" *", end="")
    print()