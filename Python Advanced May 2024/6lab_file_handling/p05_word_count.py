import re

with open('words.txt') as file:
    words = file.read()

words = words.split()

with open('text.txt') as file:
    text = file.read()

occurrences = {}

for word in words:
    pattern = rf'\b{word}\b'
    result = re.findall(pattern, text, re.IGNORECASE)
    occurrences[word] = len(result)

sorted_occ = sorted(occurrences.items(), key=lambda kvp: -kvp[1])

with open('output.txt', 'w') as file:
    for key, value in sorted_occ:
        file.write(f'{key} - {value}\n')


# Method 2
# with open('words.txt') as words_file:
#     searched_words = {}
#     for line in words_file:
#         words_per_line = line.lower().split()
#         for word in words_per_line:
#             searched_words[word] = 0
#
# pattern = r"[a-zA-Z\']+"
# text = []
#
# with open('text.txt') as text_file:
#     for line in text_file:
#         matches = re.findall(pattern, line.lower())
#         text.extend(matches)
#
# for word in searched_words:
#     if word in text:
#         searched_words[word] = text.count(word)
#
# sorted_words = sorted(searched_words.items(), key=lambda kvp: -kvp[1])
# for word, count in sorted_words:        # for item in sorted_words:
#     print(f'{word} - {count}')              # print(f"{item[0]} - {item[1]}")
