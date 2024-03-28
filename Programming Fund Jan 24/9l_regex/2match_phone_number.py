# import re
#
# phone_numbers = input()
# pattern = r'(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\b'
# matches = re.findall(pattern, phone_numbers)
# print(', '.join(matches))

import re

phone_numbers = input()
pattern = r'\+359([- ])2\1[0-9]{3}\1[0-9]{4}\b'
matches = re.finditer(pattern, phone_numbers)
found_numbers = []
for match in matches:
    found_numbers.append(match.group())
print(', '.join(found_numbers))
