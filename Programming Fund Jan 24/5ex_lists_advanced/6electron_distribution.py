electrons = int(input())
filled_shells = []
position = 0

while electrons > 0:
    position += 1
    fill = 2 * position ** 2
    if fill > electrons:
        fill = electrons
    filled_shells.append(fill)
    electrons -= fill

print(filled_shells)
