number = int(input())

for digit1 in range(1, 10):
    for digit2 in range(1, 10):
        for digit3 in range(1, 10):
            for digit4 in range(1, 10):
                if ((digit1 + digit2) == (digit3 + digit4)) and (number % (digit1 + digit2) == 0):
                    print(f'{digit1}{digit2}{digit3}{digit4}', end=' ')
