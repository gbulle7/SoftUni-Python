text = input()
encrypted_text = ''

for char in text:
    encrypted_char = chr(ord(char) + 3)
    encrypted_text += encrypted_char

print(encrypted_text)


# # print("".join([chr(ord(letter) + 3) for letter in input()]))
