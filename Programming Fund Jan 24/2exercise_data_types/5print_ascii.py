left_range = int(input())
right_range = int(input())
string = ''

for char in range(left_range, right_range + 1):
    # print(chr(char), end = ' ')
    character = chr(char)
    string += character + ' '

print(string.rstrip())