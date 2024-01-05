number = input()
my_list = list(number)
my_list.sort(reverse=True)
print(''.join(my_list))

# number = list(input())
# print(''.join((sorted(number, reverse=True))))

#number = input()
# for n in range(9, -1, -1):
#     for i in number:
#         if int(i) == int(n):
#             print(n, end="")