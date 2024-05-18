# text = input()
# chars = {}
# for char in text:
#     if char not in chars:
#         chars[char] = 0
#     chars[char] += 1
# chars_count = tuple(sorted([f'{key}: {value} time/s' for key, value in chars.items()]))
# print(*chars_count, sep='\n')

# text = tuple(input())
# chars = {}
# for char in text:
#     chars[char] = text.count(char)
# print(*sorted([f'{key}: {value} time/s' for key, value in chars.items()]), sep='\n')

txt = input()
unique_symbols = sorted(set(txt))
for char in unique_symbols:
    print(f'{char}: {txt.count(char)} time/s')
