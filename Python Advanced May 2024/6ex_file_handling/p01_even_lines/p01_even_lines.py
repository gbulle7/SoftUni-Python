symbols = ["-", ",", ".", "!", "?"]

with open('text.txt') as file:
    text = file.readlines()

for i in range(0, len(text), 2):
    line = text[i]
    for symbol in symbols:
        if symbol in line:
            line = line.replace(symbol, '@')
    print(' '.join(line.split()[::-1]))


# Method 2
with open('text.txt') as f:
    for row, line in enumerate(f.readlines()):
        if row % 2 == 0:
            for ch in "-,.!?":
                line = line.replace(ch, '@')
            print(' '.join(reversed(line.split())))


# Method 3
import re

with open('text.txt') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 2):
        line = reversed(re.sub('[-,.!?]', '@', lines[i]).split())
        print(*line)
