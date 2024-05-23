size = int(input())
moves = input().split()
field = []
field_coal = 0
m_row, m_col = 0, 0

for row in range(size):
    field.append(input().split())
    for col in range(size):
        if field[row][col] == 's':
            m_row, m_col = row, col
        elif field[row][col] == 'c':
            field_coal += 1

commands = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

for move in moves:
    new_m_row, new_m_col = commands[move](m_row, m_col)
    if new_m_row < 0 or new_m_row >= size:
        new_m_row = m_row
    if new_m_col < 0 or new_m_col >= size:
        new_m_col = m_col
    if field[new_m_row][new_m_col] == 'e':
        print(f'Game over! ({new_m_row}, {new_m_col})')
        break
    field[m_row][m_col] = '*'
    m_row, m_col = new_m_row, new_m_col
    if field[m_row][m_col] == 'c':
        field_coal -= 1
    if field_coal == 0:
        print(f'You collected all coal! ({m_row}, {m_col})')
        break
    # field[m_row][m_col] = 's'
else:
    print(f'{field_coal} pieces of coal left. ({m_row}, {m_col})')
