# 0 errors
number = int(input())
counter = 0
password = 0

for a in range(1, 9 + 1):
    for b in range(1, 9 + 1):
        for c in range(1, 9 + 1):
            for d in range(1, 9 + 1):
                if a < b and c > d:
                    calculation = a * b + c * d
                    if calculation == number:
                        print(f'{a}{b}{c}{d}', end=' ')
                        counter += 1
                        if counter == 4:
                            password = f'{a}{b}{c}{d}'
print()
if password:
    print(f'Password: {password}')
else:
    print(f'No!')

# 1 error in Judge
# number = int(input())
# iteration_count = 0
# password = 0
#
# for num in range (1111, 9999 + 1):
#     num_string = str(num)
#     if int(num_string[0]) * int(num_string[1]) + int(num_string[2]) * int(num_string[3]) == number:
#         if int(num_string[0]) < int(num_string[1]) and int(num_string[2]) > int(num_string[3]):
#             iteration_count += 1
#             if iteration_count == 4:
#                 password = num
#             print(num, end=' ')
# print()
# if password:
#     print(f'Password: {password}')
# else:
#     print(f'No!')
