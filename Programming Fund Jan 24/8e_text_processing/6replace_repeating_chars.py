string = input()
new_string = ''
last_char = ''

for char in string:
    if char == last_char:       # if char != last_char
        continue                    # new_string += char
    else:                           # last_char = char
        last_char = char
        new_string += char
print(new_string)


# def replace_repeating_characters(string):
#     for index, char in enumerate(string):
#         try:
#             if string[index + 1] != char:
#                 print(char, end='')
#         except IndexError:
#             print(char, end='')
#
#
# string = input()
# replace_repeating_characters(string)
