def merge(lst):

    first_index = int(command[1])
    second_index = int(command[2])

    if first_index < 0:
        first_index = 0
    if first_index < second_index:
        length = len(lst)
        if second_index >= length:
            second_index = length - 1
        for _ in range(first_index, second_index):
            lst[first_index] += lst.pop(first_index + 1)


def divide(lst):

    first_index = int(command[1])
    second_index = int(command[2])

    length = len(lst[first_index])
    space_between = length // second_index
    string_to_change = lst.pop(first_index)
    result = []
    for end in range(second_index - 1):
        result.append(string_to_change[:space_between])
        string_to_change = string_to_change[space_between:]
    result.append(string_to_change)
    for end in result[::-1]:
        lst.insert(first_index, end)


line = input().split()
while True:
    command = input().split()

    if command[0] == '3:1':
        break

    if command[0] == "merge":
        merge(line)

    elif command[0] == 'divide':
        divide(line)

print(' '.join(line))
