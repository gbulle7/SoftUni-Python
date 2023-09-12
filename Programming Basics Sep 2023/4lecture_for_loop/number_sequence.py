from sys import maxsize

n = int(input())
max_number = -maxsize
min_number = maxsize

for _ in range(n):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:
        min_number = current_number
print(f'Max number: {max_number}')
print(f'Min number: {min_number}')

    # by creating a list
# n = int(input())
# numbers_list = []
# for _ in range(n):
#     numbers_list.append(int(input()))
#
# max_value = max(numbers_list)
# min_value = min(numbers_list)
# print(f'Max number: {max_value}')
# print(f'Min number: {min_value}')


    # from chatgpt
# n = int(input())
# max_number = float('-inf')  # Initialize to very small value
# min_number = float('inf')   # Initialize to very large value
#
# for _ in range(n):
#     current_number = int(input())
#     if current_number > max_number:
#         max_number = current_number
#     if current_number < min_number:
#         min_number = current_number
#
# print(f'Max number: {max_number}')
# print(f'Min number: {min_number}')