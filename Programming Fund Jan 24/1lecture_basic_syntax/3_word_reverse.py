word = input()
reversed_word = ''

for index in range(len(word) - 1, -1, -1):
    reversed_word += word[index]
print(reversed_word)

# word = input()
# print(word[::-1])