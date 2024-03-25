sequence = input().split()
result = ''

for word in sequence:
    result += word * len(word)

print(result)
