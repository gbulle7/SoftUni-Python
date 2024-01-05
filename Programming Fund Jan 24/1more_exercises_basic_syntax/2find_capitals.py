# string = input()
# my_list = []
#
# for index, char in enumerate(string):
#     if char.isupper():
#         my_list.append(index)
# print(my_list)

string = input()
my_list = []

for char in range(len(string)):
    if string[char].isupper():
        my_list.append(char)
print(my_list)