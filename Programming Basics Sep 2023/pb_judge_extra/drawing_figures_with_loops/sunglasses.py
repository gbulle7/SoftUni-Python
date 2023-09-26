number = int(input())
connection = ''

print(2 * number * '*' + number * ' ' + 2 * number * '*')
for row in range(number-2):
    if row == (number - 1) // 2 - 1:
        connection = '|'
    else:
        connection = ' '
    print(f'*{(number * 2 - 2) * "/"}*{number * connection}*{(number * 2 - 2) * "/"}*')
print(2 * number * '*' + number * ' ' + 2 * number * '*')