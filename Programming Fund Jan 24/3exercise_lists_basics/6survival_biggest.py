from math import inf

my_list = [int(integer) for integer in input().split()]
remove_count = int(input())

for _ in range(remove_count):
    min_value = +inf
    for num in my_list:
        if num < min_value:
            min_value = num
    my_list.remove(min_value)

my_list_string = list(map(str, my_list))
output = ', '.join(my_list_string)

print(output)