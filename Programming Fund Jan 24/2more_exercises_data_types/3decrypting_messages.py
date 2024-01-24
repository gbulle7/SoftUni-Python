key = int(input())
lines = int(input())
message = []

for char in range(lines):
    letter = input()
    message.append(chr(ord(letter) + key))

print(''.join(message))
