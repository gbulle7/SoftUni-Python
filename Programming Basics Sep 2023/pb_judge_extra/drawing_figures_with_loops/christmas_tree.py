# number = int(input())
#
# print(number * ' ', '|')
# for row in range(number):
#     print((number-row-1)*' ' + (row+1) * '*', '|', (row+1) * '*')

count = int(input())

for i in range(count + 1):
    print(f"{' ' * (count - i)}{'*' * i} | {'*' * i}")
