import re

text = input()
pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group(), end=' ')


# import re
#
# text = input()
# pattern = r'(^|(?<=\s))(-?)([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
# matches = re.findall(pattern, text)
# for match in matches:
#     match = match[0] + match[1] + match[2] + match[3] + match[4]
#     print(match, end=' ')
