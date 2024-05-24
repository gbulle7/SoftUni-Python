size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

while True:
    command = input()
    if command == 'END':
        break
    cmd, r, c, value = command.split()
    r, c, value = int(r), int(c), int(value)
    if r not in range(size) or c not in range(size):
        print('Invalid coordinates')
        continue
    if cmd == 'Add':
        matrix[r][c] += value
    elif cmd == 'Subtract':
        matrix[r][c] -= value

[print(*row) for row in matrix]
