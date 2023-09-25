number1 = int(input())
number2 = int(input())
number3 = int(input())
digit1 = 0
digit2 = 0
digit3 = 0

for num1 in range(2, number1 + 1):
    if num1 % 2 == 0:
        digit1 = num1
    else:
        continue
    for num2 in range(2, number2 + 1):
        if num2 % 2 == 0 and num2 != 2:
            continue
        elif num2 > 7:
            continue
        else:
            digit2 = num2
        for num3 in range(2, number3 + 1):
            if num3 % 2 == 0:
                digit3 = num3
                print(f'{digit1} {digit2} {digit3}')
