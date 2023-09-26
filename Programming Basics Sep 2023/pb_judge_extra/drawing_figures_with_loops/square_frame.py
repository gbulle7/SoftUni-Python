# method 1
number = int(input())

print(f'+{" -" * (number - 2)} +')

for mid_row in range(number - 2):
    print(f'|{" -" * (number - 2)} |')

print(f'+{" -" * (number - 2)} +')

# method 2
# number = int(input())
#
# print('+', end=' ')
# for top_row in range(number - 2):
#     print('-', end=' ')
# print('+')
#
# for mid_row in range(number - 2):
#     print('|',end=' ')
#     for mid_column in range(number - 2):
#         print('-',end=' ')
#     print('|')
#
# print('+', end=' ')
# for bottom_row in range(number - 2):
#     print('-', end=' ')
# print('+')
