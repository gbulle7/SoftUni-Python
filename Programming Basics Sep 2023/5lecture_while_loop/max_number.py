# with while True
import math

max_number = -math.inf

while True:
    text = input()
    if text == 'Stop':
        break
    number = int(text)
    if number > max_number:
        max_number = number
print(max_number)

# with while
# import math
#
# text = input()
# max_number = -math.inf
#
# while text != 'Stop':
#     current_number = int(text)
#     if current_number > max_number:
#         max_number = current_number
#     text = input()
# print(max_number)