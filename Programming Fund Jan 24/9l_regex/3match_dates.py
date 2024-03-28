import re

dates = input()
pattern = r'\b(?P<day>\d{2})([-./])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b'
matches = re.finditer(pattern, dates)
for match in matches:
    day = match.group('day')
    month = match.group('month')
    year = match.group('year')
    print(f'Day: {day}, Month: {month}, Year: {year}')


# import re
#
# text = input()
# pattern = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'
# matches = re.findall(pattern, text)
# for match in matches:
#     day = match[0]
#     month = match[2]
#     year = match[3]
#     print(f'Day: {day}, Month: {month}, Year: {year}')


# import re
#
# text = input()
# pattern = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'
# matches = re.finditer(pattern, text)
#
# for match in matches:
#     day = match.group(1)
#     month = match.group(3)
#     year = match.group(4)
#     print(f'Day: {day}, Month: {month}, Year: {year}')
