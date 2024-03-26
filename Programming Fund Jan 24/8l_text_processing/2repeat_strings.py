sequence = input().split()
result = ''

for word in sequence:
    result += word * len(word)

print(result)

# data = input().split()
# repeat_text = [text * len(text) for text in data]
# print(''.join(repeat_text))
