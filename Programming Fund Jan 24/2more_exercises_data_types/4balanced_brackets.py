lines = int(input())
brackets = ['']
balanced = True

for char in range(lines):

    letter = input()
    if letter == '(':
        if brackets[-1] == '(':
            balanced = False
            break
        brackets.append(letter)
    elif letter == ')':
        if brackets[-1] != '(':
            balanced = False
            break
        brackets.append(letter)

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')


