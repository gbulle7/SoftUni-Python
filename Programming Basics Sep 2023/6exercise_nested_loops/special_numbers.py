number = int(input())

for current_number in range(1111, 9999 + 1):
    string_number = str(current_number)
    is_special = True
    for digit in string_number:
        if int(digit) == 0 or number % int(digit) != 0:
            is_special = False
            break
    if is_special:
        print(current_number, end=' ')

# method 1
# number = int(input())
#
# for current_number in range(1111, 9999 + 1):
#     string_number = str(current_number)
#     is_special = True
#     for index, digit in enumerate(string_number):
#         if int(digit) == 0 or number % int(digit) != 0:
#             is_special = False
#             break
#     if is_special:
#         print(current_number, end=' ')

# method 2
# number = int(input())
#
# for current_number in range(1111, 10000):
#     string_number = str(current_number)
#     is_special = True
#     for digit in range(len(string_number)):
#
#         if int(string_number[digit]) == 0 or number % int(string_number[digit]) != 0:
#             is_special = False
#             break
#     if is_special:
#         print(current_number, end=' ')