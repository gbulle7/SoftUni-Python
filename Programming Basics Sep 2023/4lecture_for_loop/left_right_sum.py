n = int(input())
sum1 = 0
sum2 = 0

for _ in range(n):
    number1 = int(input())
    sum1 += number1
for _ in range(n):
    number2 = int(input())
    sum2 += number2

if sum1 == sum2:
    print(f'Yes, sum = {sum1}')
else:
    difference = abs(sum1 - sum2)
    print(f'No, diff = {difference}')

    # only with 1 for loop
#n = int(input())
# left_sum = 0
# right_sum = 0
#
# for numbers in range(n * 2):
#     current_number = int(input())
#     if numbers < n:
#         left_sum += current_number
#     else:
#         right_sum += current_number
# if left_sum == right_sum:
#     print(f'Yes, sum = {left_sum}')
# else:
#     difference = abs(left_sum - right_sum)
#     print(f'No, diff = {difference}')
