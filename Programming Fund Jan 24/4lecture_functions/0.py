# lst = [1, 2, 3]
#
# number = [x ** 2 for x in lst]
# print(number)

lst = [1, 2, 3]

number = list(map(lambda x: x ** 2, lst))
print(number)