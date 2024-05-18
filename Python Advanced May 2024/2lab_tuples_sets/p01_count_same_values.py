# numbers = tuple(float(x) for x in input().split())
# # numbers = tuple(map(float, input().split()))
# values_count = {}
# for num in numbers:
#     if num not in values_count:
#         values_count[num] = 0
#     values_count[num] += 1
#
# [print(f'{key} - {value} times') for key, value in values_count.items()]

numbers = tuple(float(x) for x in input().split())
values_count = {}
for num in numbers:
    if num not in values_count:
        values_count[num] = numbers.count(num)
[print(f'{key:.1f} - {value} times') for key, value in values_count.items()]
