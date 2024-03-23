words = input().split()
# words = [char for char in input() if char != " "]
occurrences = {}

for word in words:
    for char in word:
        if char not in occurrences:
            occurrences[char] = 0
        occurrences[char] += 1

for key, value in occurrences.items():
    print(f'{key} -> {value}')


# Using Counter
# from collections import Counter
#
# word = ''.join(input().split())
# chars_dict = Counter(word)
#
# for k, v in chars_dict.items():
#     print(f'{k} -> {v}')

