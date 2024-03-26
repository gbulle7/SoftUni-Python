string = input()
new_string = ''
strength = 0

for index in range(len(string)):
    if string[index] == '>':
        strength += int(string[index+1])
        new_string += string[index]
    elif strength > 0 and string[index] != '>':
        strength -= 1
    else:
        new_string += string[index]

print(new_string)
