# number = int(input())
# my_list = []
# filtered = []
#
# for _ in range(number):
#     integer = int(input())
#     my_list.append(integer)
#
# command = input()
#
# if command == 'even':
#     for num in my_list:
#         if num % 2 == 0:
#             filtered.append(num)
# elif command == 'odd':
#     for num in my_list:
#         if num % 2 != 0:
#             filtered.append(num)
# elif command == 'negative':
#     for num in my_list:
#         if num < 0:
#             filtered.append(num)
# elif command == 'positive':
#     for num in my_list:
#         if num >= 0:
#             filtered.append(num)
#
# print(filtered)


n = int(input())
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_POSITIVE = 'positive'
COMMAND_NEGATIVE = 'negative'

numbers = [int(input()) for _ in range(n)]
filtered_numbers = []
command = input()

for num in numbers:
    filtered_command = (
        (command == COMMAND_EVEN and num % 2 == 0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_POSITIVE and num >= 0) or
        (command == COMMAND_NEGATIVE and num < 0)
    )

    if filtered_command:
        filtered_numbers.append(num)

print(filtered_numbers)
