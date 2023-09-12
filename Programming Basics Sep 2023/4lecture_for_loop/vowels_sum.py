text = input()
sum = 0

for vowel in text:
    if vowel == 'a':
        sum += 1
    elif vowel == 'e':  # moje if vmesto eilf
        sum += 2
    elif vowel == 'i':  # moje if vmesto eilf
        sum += 3
    elif vowel == 'o':  # moje if vmesto eilf
        sum += 4
    elif vowel == 'u':  # moje if vmesto eilf
        sum += 5
print(sum)

# for vowel in range(len(text)):  # range(len(text)) = range(0, len(text))
#     if text[vowel] == 'a':
#         sum += 1
#     if text[vowel] == 'e':
#         sum += 2
#     if text[vowel] == 'i':
#         sum += 3
#     if text[vowel] == 'o':
#         sum += 4
#     if text[vowel] == 'u':
#         sum += 5
# print(sum)
