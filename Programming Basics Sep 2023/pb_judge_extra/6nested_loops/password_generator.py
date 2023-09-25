number_n = int(input())
number_l = int(input())

for symbol1 in range(1, number_n):
    for symbol2 in range(1, number_n):
        for symbol3 in range(ord('a'), ord('a') + number_l):
            for symbol4 in range(ord('a'), ord('a') + number_l):
                for symbol5 in range(1, number_n + 1):
                    if symbol5 > symbol1 and symbol5 > symbol2:
                        print(f'{symbol1}{symbol2}{chr(symbol3)}{chr(symbol4)}{symbol5} ', end='')
