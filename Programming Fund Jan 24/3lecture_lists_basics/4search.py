number = int(input())
word = input()
my_list = []

for _ in range(number):
    string = input()
    my_list.append(string)

print(my_list)

for index in range(len(my_list) - 1, -1, -1):
    if word not in my_list[index]:
        my_list.remove(my_list[index])

print(my_list)
