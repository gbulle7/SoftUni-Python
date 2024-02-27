initial_list = [int(integer) for integer in input().split()]
command = input().split()

while command[0] != 'end':
    even = [num for num in initial_list if num % 2 == 0]
    odd = [num for num in initial_list if num % 2 != 0]

    if command[0] == 'exchange':
        if 0 <= int(command[1]) < len(initial_list):
            initial_list = initial_list[int(command[1]) + 1:] + initial_list[:int(command[1]) + 1]
        else:
            print('Invalid index')

    elif command[0] == 'max':
        if command[1] == 'even' and even:
            print(len(initial_list) - initial_list[::-1].index(max(even)) - 1)
        elif command[1] == 'odd' and odd:
            print(len(initial_list) - initial_list[::-1].index(max(odd)) - 1)
        else:
            print('No matches')

    elif command[0] == 'min':
        if command[1] == 'even' and even:
            print(len(initial_list) - initial_list[::-1].index(min(even)) - 1)
        elif command[1] == 'odd' and odd:
            print(len(initial_list) - initial_list[::-1].index(min(odd)) - 1)
        else:
            print('No matches')

    elif command[0] == 'first':
        if int(command[1]) <= len(initial_list):
            if command[2] == 'even':
                print(even[:int(command[1])])
            elif command[2] == 'odd':
                print(odd[:int(command[1])])
        else:
            print('Invalid count')

    elif command[0] == 'last':
        if int(command[1]) <= len(initial_list):
            if command[2] == 'even':
                print(even[-int(command[1]):])
            elif command[2] == 'odd':
                print(odd[-int(command[1]):])
        else:
            print('Invalid count')

    command = input().split()

print(initial_list)