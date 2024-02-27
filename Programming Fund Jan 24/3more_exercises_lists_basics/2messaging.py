numbers = input().split()
words = list(input())

message = []

for number in numbers:
    sum_digits = 0
    for digit in number:
        sum_digits += int(digit)

    if sum_digits >= len(words):
        sum_digits -= len(words)
    # sum_digits %= len(words)

    for letter in range(len(words)):
        if letter == sum_digits:
            character = words.pop(letter)
            message.append(character)
print(''.join(message))
