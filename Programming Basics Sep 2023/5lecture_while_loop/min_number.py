# with while True
from math import inf

min_number = inf

while True:
    text = input()
    if text == 'Stop':
        break
    number = int(text)
    if number < min_number:
        min_number = number
print(min_number)

# with while
# from math import inf
#
# min_number = inf
#
# text = input()
#
# while text != 'Stop':
#     number = int(text)
#     if number < min_number:
#         min_number = number
#     text = input()
# print(min_number)