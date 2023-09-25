a = int(input())
b = int(input())
max_passwords = int(input())
x = 0
y = 0
symbol1 = 35
symbol2 = 64
is_full = False

for x in range(1, a + 1):
    for y in range(1, b + 1):
        if x == a + 1 and y == b + 1:
            is_full = True
            break
        if symbol1 > 55:
            symbol1 = 35
        if symbol2 > 96:
            symbol2 = 64
        print(f'{chr(symbol1)}{chr(symbol2)}{x}{y}{chr(symbol2)}{chr(symbol1)}|', end='')
        symbol1 += 1
        symbol2 += 1
        max_passwords -= 1
        if max_passwords <= 0:
            is_full = True
            break
    if is_full:
        break