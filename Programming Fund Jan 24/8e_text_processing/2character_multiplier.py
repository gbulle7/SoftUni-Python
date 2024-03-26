first_string, second_string = input().split()
sum = 0

if len(first_string) < len(second_string):
    primary = first_string
    secondary = second_string
else:
    primary = second_string
    secondary = first_string

for index in range(len(primary)):
    sum += ord(primary[index]) * ord(secondary[index])

for index in range(len(primary), len(secondary)):
    sum += ord(secondary[index])

print(sum)


# def characters_multiply(first_string, second_string):
#     first_string = [ord(num) for num in first_string]
#     second_string = [ord(num) for num in second_string]
#     first_string_len = len(first_string)
#     second_string_len = len(second_string)
#     if first_string_len > second_string_len:
#         for index in range(first_string_len - second_string_len):
#             second_string.append(1)
#     elif first_string_len < second_string_len:
#         for index in range(second_string_len - first_string_len):
#             first_string.append(1)
#     print(sum([first_string[index] * second_string[index] for index in range(len(first_string))]))
#
#
# string_one, string_two = input().split()
# characters_multiply(string_one, string_two)


# first_string, second_string = input().split()
# total_sum = 0
# if len(first_string) > len(second_string):
#     # Here we have multiplication
#     for index in range(len(second_string)):
#         total_sum += ord(first_string[index]) * ord(second_string[index])
#     # Here we are adding the rest of the first string
#     for index in range(len(second_string), len(first_string)):
#         total_sum += ord(first_string[index])
# elif len(second_string) > len(first_string):
#     # Here we have multiplication
#     for index in range(len(first_string)):
#         total_sum += ord(first_string[index]) * ord(second_string[index])
#     # Here we are adding the rest of the first string
#     for index in range(len(first_string), len(second_string)):
#         total_sum += ord(second_string[index])
# else:  # elif len(first_string) == len(second_string)
#     # Here we have multiplication
#     for index in range(len(second_string)):
#         total_sum += ord(first_string[index]) * ord(second_string[index])
# print(total_sum)