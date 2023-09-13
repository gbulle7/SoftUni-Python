import math

number = int(input())
max_number = -math.inf
total_sum = 0

for _ in range(number):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_number:
        max_number = current_number
difference = abs(total_sum - max_number)
if difference == max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    difference -= max_number
    print('No')
    print(f'Diff = {abs(difference)}')
