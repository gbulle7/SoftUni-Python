string = ''
output = ''

while True:
    string = input()
    if string == 'SoftUni':
        continue
    if string == 'End':
        break
    for letter in range(len(string)):
        output += string[letter] * 2
    print(output)
    output = ''


