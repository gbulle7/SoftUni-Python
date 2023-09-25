men = int(input())
women = int(input())
max_tables = int(input())
is_full = False

for man in range(1, men + 1):
    for woman in range(1, women + 1):
        print(f'({man} <-> {woman})', end=' ')
        max_tables -= 1
        if max_tables <= 0:
            is_full = True
            break
    if is_full:
        break
