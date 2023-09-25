cent_limit = int(input())
deci_limit = int(input())
digit_limit = int(input())

for cent in range(1, cent_limit + 1):
    if cent % 2 != 0:
        continue
    for deci in range(2, deci_limit + 1):
        if deci > 7:
            continue
        if deci % 2 == 0 and deci != 2:
            continue
        for digit in range(1, digit_limit + 1):
            if digit % 2 != 0:
                continue
            print(f'{cent} {deci} {digit}')
