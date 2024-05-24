size = int(input())
matrix = []
a_row, a_col = (0, 0)
collected_teabags = 0

for row in range(size):
    curr_row = [int(x) if x.isdigit() else x for x in input().split()]
    matrix.append(curr_row)
    if "A" in curr_row:
        a_row, a_col = row, curr_row.index("A")

commands = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

has_lost = False

while True:
    matrix[a_row][a_col] = '*'
    if collected_teabags >= 10:
        print(f"She did it! She went to the party.")
        break
    new_a_row, new_a_col = commands[input()](a_row, a_col)
    if new_a_row not in range(size) or new_a_col not in range(size):
        has_lost = True
        break
    if matrix[new_a_row][new_a_col] == 'R':
        matrix[new_a_row][new_a_col] = '*'
        has_lost = True
        break
    if matrix[new_a_row][new_a_col] in range(1, 11):
        collected_teabags += matrix[new_a_row][new_a_col]
    a_row, a_col = new_a_row, new_a_col

if has_lost:
    print(f"Alice didn't make it to the tea party.")
[print(*row) for row in matrix]
