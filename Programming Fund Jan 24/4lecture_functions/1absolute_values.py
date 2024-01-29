number = input().split()
absolute_numbers = []

for num in number:
    abs_num = abs(float(num))
    absolute_numbers.append(abs_num)

print(absolute_numbers)

# w/ List Comprehension
# absolute_numbers = [abs(float(num)) for num in input().split()]
# print(absolute_numbers)
