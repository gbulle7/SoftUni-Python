def odd_even_sum(num):
    odd_sum = 0
    even_sum = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    output = f'Odd sum = {odd_sum}, Even sum = {even_sum}'
    return output


number = int(input())
print(odd_even_sum(number))


# def even_odd_sum(nums, even, odd):
#     for index in range(len(nums)):
#         current_number = int(nums[index])
#         if current_number % 2 == 0:
#             even += current_number
#         else:
#             odd += current_number
#
#     return f'Odd sum = {odd}, Even sum = {even}'
#
#
# numbers = input()
# even_sum = 0
# odd_sum = 0
# print(even_odd_sum(numbers, even_sum, odd_sum))
