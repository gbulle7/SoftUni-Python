characters = input().split(', ')
char_dict = {key: ord(key) for key in characters}
print(char_dict)

# print({char: ord(char) for char in input().split(", ")})

# characters = input().split(", ")
#
# letters = {}
#
# for letter in characters:
#     letters[letter] = ord(letter)
#
# print(letters)