my_list = list(map(int, input().split(', ')))
count = my_list.count(0)
while count > 0:
    my_list.remove(0)
    my_list.append(0)
    count -= 1
print(my_list)

# my_list = list(map(int, input().split(', ')))
# for digit in my_list:
#     my_list.remove(0)
#     my_list.append(0)
# print(my_list)
