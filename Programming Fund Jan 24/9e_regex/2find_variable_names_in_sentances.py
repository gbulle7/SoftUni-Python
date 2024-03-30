import re

text = input()

# pattern = r'(?<= _)[a-zA-Z0-9]+\b'
# match = re.findall(pattern, text)
# print(','.join(match))

pattern = r'\b_([a-zA-Z0-9]+)\b'
match = re.findall(pattern, text)
print(','.join(match))
