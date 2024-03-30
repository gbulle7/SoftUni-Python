import re

line = input()
word = input()

pattern = fr'(?i){word}\b'            # pattern = fr'{word}\b'
match = re.findall(pattern, line)     # match = re.findall(pattern, line, re.IGNORECASE)
print(len(match))
