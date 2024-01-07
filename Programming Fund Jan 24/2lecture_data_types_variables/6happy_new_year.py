year = int(input())

while True:
    year += 1
    my_list = list(str(year))
    my_set = set(str(year))
    if len(my_set) == len(my_list):
        break

print(year)

# year = int(input())
#
# while True:
#     year += 1
#     is_happy_year = True
#     already_found_digits = ''
#     for digit in str(year):
#         if digit in already_found_digits:
#             is_happy_year = False
#             break
#         already_found_digits += digit
#     if is_happy_year:
#         break
#
# print(year)
