# optimised
start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

combinations = 0
condition = False
text_information = ''

for num1 in range(start_interval, end_interval + 1):
    for num2 in range(start_interval, end_interval + 1):
        combinations += 1
        if num1 + num2 == magic_number:
            condition = True
            text_information = f'Combination N:{combinations} ({num1} + {num2} = {magic_number})'
            break
    if condition:
        break

if condition:
    print(text_information)
else:
    print(f'{combinations} combinations - neither equals {magic_number}')

# my task
# left_range = int(input())
# right_range = int(input())
# magic_number = int(input())
# combinations = 0
# number1 = 0
# number2 = 0
# flag = False
#
# for number1 in range(left_range, right_range + 1):
#     for number2 in range(left_range, right_range + 1):
#         result = number1 + number2
#         combinations += 1
#         if result == magic_number:
#             flag = True
#             break
#     if flag:
#         print(f'Combination N:{combinations} ({number1} + {number2} = {magic_number})')
#         break
# else:
#     print(f'{combinations} combinations - neither equals {magic_number}')
