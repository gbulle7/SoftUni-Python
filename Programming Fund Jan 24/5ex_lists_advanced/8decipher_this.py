secret_message = input().split()

for value in secret_message:
    number = ''
    chars = ''
    for letter in value:

        if letter.isnumeric():  # isdigit(); isdecimal()
            number += letter
        else:
            chars += letter
    word = chr(int(number)) + chars
    word = [*word]
    word[1], word[-1] = word[-1], word[1]
    print(''.join(word), end=' ')
