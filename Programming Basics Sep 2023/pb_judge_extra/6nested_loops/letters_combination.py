character1 = input()
character2 = input()
character3 = input()
combinations = 0

for char1 in range(ord(character1), ord(character2) + 1):
    if char1 == ord(character3):
        continue
    for char2 in range(ord(character1), ord(character2) + 1):
        if char2 == ord(character3):
            continue
        for char3 in range(ord(character1), ord(character2) + 1):
            if char3 == ord(character3):
                continue
            combinations += 1
            print(f'{chr(char1)}{chr(char2)}{chr(char3)}', end=' ')
print(combinations)