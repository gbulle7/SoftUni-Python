# string = input()
#
# my_list = string.split()
# opposite_list = []
#
# for element in my_list:
#     opposite_element = int(element) * -1
#     opposite_list.append(opposite_element)
#
# print(opposite_list)

# w/ List Comprehension
print([-int(number) for number in input().split()])
