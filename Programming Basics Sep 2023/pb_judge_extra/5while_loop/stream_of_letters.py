c = 0
o = 0
n = 0
letter = ''
current_word = ''
sentence = ''

while True:
    if c > 0 and o > 0 and n > 0:
        sentence += current_word + ' '
        current_word = ''
        c = 0
        n = 0
        o = 0
    letter = input()
    if letter == 'End':
        break
    if letter.isalpha() != True:
        continue
    if letter == 'c' and c == 0:
        c += 1
        continue
    elif letter == 'o' and o == 0:
        o += 1
        continue
    elif letter == 'n' and n == 0:
        n += 1
        continue
    current_word += letter
print(sentence)


