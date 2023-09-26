number = int(input())

for row in range(1, (number + 3) // 2):
    if row == 1:
        if number % 2 == 0:
            print(f"{'-' * ((number - 2) // 2)}**{'-' * ((number - 2) // 2)}")
        else:
            print(f"{'-' * ((number - 1) // 2)}*{'-' * ((number - 1) // 2)}")
    else:
        if number % 2 == 0:
            print(f"{'-' * ((number - (row - 1) * 2 - 2) // 2)}*{'-' * ((row - 1) * 2)}*{'-' * ((number - (row - 1) * 2 - 2) // 2)}")
        else:
            print(f"{'-' * ((number - (row - 1) * 2 - 1) // 2)}*{'-' * ((row - 1) * 2 - 1)}*{'-' * ((number - (row - 1) * 2 - 1) // 2)}")

for row in range((number - 1) // 2, 0, -1):
    if row == 1:
        if number % 2 == 0:
            print(f"{'-' * ((number - 2) // 2)}**{'-' * ((number - 2) // 2)}")
        else:
            print(f"{'-' * ((number - 1) // 2)}*{'-' * ((number - 1) // 2)}")
    else:
        if number % 2 == 0:
            print(f"{'-' * ((number - (row - 1) * 2 - 2) // 2)}*{'-' * ((row - 1) * 2)}*{'-' * ((number - (row - 1) * 2 - 2) // 2)}")
        else:
            print(f"{'-' * ((number - (row - 1) * 2 - 1) // 2)}*{'-' * ((row - 1) * 2 - 1)}*{'-' * ((number - (row - 1) * 2 - 1) // 2)}")
