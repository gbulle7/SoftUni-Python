string = input().split()
result = 0

for word in string:
    left_char = word[0]
    right_char = word[-1]
    number = int(word[1: len(word) - 1])

    if left_char.isupper():
        number /= (ord(left_char) - 64)
    elif left_char.islower():
        number *= (ord(left_char) - 96)
    if right_char.isupper():
        number -= (ord(right_char) - 64)
    elif right_char.islower():
        number += (ord(right_char) - 96)

    result += number
print(f'{result:.2f}')


# string = input().split()
# result = 0
#
# for word in string:
#     left_char = word[0]
#     right_char = word[-1]
#     mid_string = ''
#     for char in range(1, len(word) - 1):
#         mid_string += word[char]
#
#     number = float(mid_string)
#
#     if left_char.isupper():
#         number /= (ord(left_char.lower()) - 96)
#     elif left_char.islower():
#         number *= (ord(left_char) - 96)
#     if right_char.isupper():
#         number -= (ord(right_char.lower()) - 96)
#     elif right_char.islower():
#         number += (ord(right_char) - 96)
#
#     result += number
# print(f'{result:.2f}')


# import re
#
# main_string = re.sub("\s+", " ", input()).split()
# total = 0
# for string in main_string:
#     numbers = int(string[1:-1])
#     if string[0].isupper():
#         first_result = numbers / ((ord(string[0].lower())) - 96)
#     else:
#         first_result = numbers * ((ord(string[0].lower())) - 96)
#
#     if string[-1].isupper():
#         second_result = first_result - ((ord(string[-1].lower())) - 96)
#     else:
#         second_result = first_result + ((ord(string[-1].lower())) - 96)
#     total += second_result
#
# print(f"{total:.2f}")