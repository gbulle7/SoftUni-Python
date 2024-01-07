number = int(input())

for num in range(1, number + 1):
    sum_digits = 0
    is_special = False

    for digit in str(num):
        sum_digits += int(digit)
    if sum_digits in (5, 7, 11):
        is_special = True

    print(f'{num} -> {is_special}')

# number = int(input())
#
# for num in range(1, number + 1):
#     sum_digits = 0
#     digits = num
#
#     while digits > 0:
#         sum_digits += digits % 10
#         digits = int(digits/10)
#     if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
#         print(f'{num} -> True')
#     else:
#         print(f'{num} -> False')