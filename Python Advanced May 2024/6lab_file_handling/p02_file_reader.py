file = open('numbers.txt', 'r')
numbers_sum = 0
for number in file:
    numbers_sum += int(number)
print(numbers_sum)

# sum_numbers = 0
# text = file.readlines()
# for line in text:
#     sum_numbers += int(line[:-1])
# print(sum_numbers)
