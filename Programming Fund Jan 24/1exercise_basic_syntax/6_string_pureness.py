number = int(input())
pure = True

for _ in range(number):
    string = input()
    for letter in range(len(string)):
        if string[letter] == '.' or string[letter] == ',' or string[letter] == '_':
            pure = False
            break
    if pure:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')
    pure = True

# n = int(input())
# for _ in range(n):
#     string = input()
#     if '.' in string or '_' in string or ',' in string:
#         print(f'{string} is not pure!')
#     else:
#         print(f'{string} is pure.')
