import re

pattern = r'\d+'
text = ''
while True:
    line = input()
    if not line:
        break
    text += line

match = re.findall(pattern, text)
print(' '.join(match))



# import re
#
# line = input()
# while line:
#     pattern = "\d+"
#     matches = re.findall(pattern, line)
#     if matches:
#         print(" ".join(matches), end = " ")
#     line = input()


# import re
# pattern = r'\d+'
# digits = []
# while True:
#     string = input()
#     if string:
#         numbers = re.findall(pattern, string)
#         if numbers:
#             digits.append(' '.join(numbers))
#         continue
#     break
#
# print(' '.join(digits))
