# method 1
sum_prime = 0
sum_non_prime = 0
is_prime = 0

while True:
    command = input()
    if command == 'stop':
        break
    current_number = int(command)
    if current_number < 0:
        print('Number is negative.')
        continue
    for number in range(1, current_number + 1):
        if current_number % number == 0:
            is_prime += 1
    if is_prime != 2:
        sum_non_prime += current_number
    else:
        sum_prime += current_number
    is_prime = 0
print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')

# method 2 optimised
# command = input()
# sum_prime = 0
# sum_non_prime = 0
#
# while command != 'stop':
#     current_number = int(command)
#     if current_number < 0:
#         print('Number is negative.')
#     else:
#         is_prime = True
#         for number in range(2, current_number):
#             if current_number % number == 0:    # curent number is not prime
#                 is_prime = False
#                 break
#         if is_prime:
#             sum_prime += current_number
#         else:
#             sum_non_prime += current_number
#     command = input()
# print(f'Sum of all prime numbers is: {sum_prime}')
# print(f'Sum of all non prime numbers is: {sum_non_prime}')
