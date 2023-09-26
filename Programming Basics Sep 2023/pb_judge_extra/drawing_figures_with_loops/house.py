number = int(input())

for roof_row in range((number + 1) // 2):
    if roof_row == 0:
        if number % 2 == 0:
            print(f"{'-' * ((number - 2) // 2)}**{'-' * ((number - 2) // 2)}")
        else:
            print(f"{'-' * ((number - 1) // 2)}*{'-' * ((number - 1) // 2)}")
    else:
        if number % 2 == 0:
            print(f"{'-' * ((number - (roof_row + 1) * 2) // 2)}{'*' * ((roof_row + 1) * 2)}{'-' * ((number - (roof_row + 1) * 2) // 2)}")
        else:
            print(f"{'-' * ((number + 1 - (roof_row + 1) * 2) // 2)}{'*' * ((roof_row + 1) * 2 - 1)}{'-' * ((number + 1 - (roof_row + 1) * 2) // 2)}")

for base_row in range (number - (number + 1) // 2):
    print(f"|{'*' * (number - 2)}|")