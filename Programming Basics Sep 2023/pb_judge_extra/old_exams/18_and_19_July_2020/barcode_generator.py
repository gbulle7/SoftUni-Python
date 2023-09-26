start_interval = int(input())
end_interval = int(input())
start_interval_str = str(start_interval)
end_interval_str = str(end_interval)

for num1 in range(int(start_interval_str[0]), int(end_interval_str[0]) + 1):
    for num2 in range(int(start_interval_str[1]), int(end_interval_str[1]) + 1):
        for num3 in range(int(start_interval_str[2]), int(end_interval_str[2]) + 1):
            for num4 in range(int(start_interval_str[3]), int(end_interval_str[3]) + 1):
                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f'{num1}{num2}{num3}{num4} ', end='')
