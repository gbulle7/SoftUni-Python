numbers = input().split(', ')
indices = []
for index, number in enumerate(numbers):
    if int(number) % 2 == 0:
        indices.append(index)

print(indices)


# list_numbers = list(map(int, input().split(', ')))
# even_numbers = [index for index in range(len(list_numbers)) if list_numbers[index] % 2 == 0]
# print(even_numbers)


# numbers = input().split(', ')
# even_numbers = [index for index in range(len(numbers)) if int(numbers[index]) % 2 == 0]
# print(even_numbers)
