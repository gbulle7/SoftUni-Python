def characters_range(chr1, chr2):
    for character in range(ord(chr1) + 1, ord(chr2)):
        chars_list.append(chr(character))
    return ' '.join(chars_list)


char1 = input()
char2 = input()
chars_list = []

result = characters_range(char1, char2)
print(result)


# def characters(first, second):
#
#     for chars in range(ord(first) + 1, ord(second)):
#         print(chr(chars), end=' ')
#
#
# first_character = input()
# second_character = input()
# characters(first_character, second_character)


# chars_range = lambda char1, char2: ' '.join(map(chr, range(ord(char1) + 1, ord(char2))))
# character1 = input()
# character2 = input()
# print(chars_range(character1, character2))