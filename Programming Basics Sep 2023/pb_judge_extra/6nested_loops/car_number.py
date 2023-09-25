start_interval = int(input())
end_interval = int(input())

for digit1 in range(start_interval, end_interval + 1):
    for digit2 in range(start_interval, end_interval + 1):
        for digit3 in range(start_interval, end_interval + 1):
            for digit4 in range(start_interval, digit1):
                if (digit2 + digit3) % 2 == 0:
                    if digit1 % 2 == 0 and digit4 % 2 != 0 or digit1 % 2 != 0 and digit4 %2 == 0:
                        print(f'{digit1}{digit2}{digit3}{digit4}', end=' ')