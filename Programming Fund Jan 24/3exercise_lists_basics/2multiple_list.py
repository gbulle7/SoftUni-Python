factor = int(input())
count = int(input())

my_list = []

for multiplier in range(1, count + 1):
    my_list.append(factor * multiplier)
print(my_list)

# factor_number = int(input())
# count_number = int(input())
#
# my_list = []
# number = factor_number
#
# while len(my_list) < count_number:
#     if number % factor_number == 0:
#         my_list.append(number)
#     number += 1
#
# print(my_list)

# factor_number = int(input())
# count_number = int(input())
# add = factor_number
# my_list = []
# for _ in range(count_number):
#     my_list.append(factor_number)
#     factor_number += add
# print(my_list)