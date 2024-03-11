# wagons = int(input())
# train = [0 for wagon in range(wagons)]
# command = input().split()
#
# while command[0] != 'End':
#     if command[0] == 'add':
#         train[-1] += (int(command[1]))
#     elif command[0] == 'insert':
#         train[int(command[1])] += int(command[2])
#     elif command[0] == 'leave':
#         train[int(command[1])] -= int(command[2])
#     command = input().split()
#
# print(train)

# def train_passangers(wgons):
#     train = [0] * wgons
#
#     while True:
#         command = input().split()
#         if command[0] == 'End':
#             break
#         cmd = command[0]
#         index = int(command[1])
#         people = int(command[-1])
#
#         if cmd == 'add':
#             train[-1] += people
#         elif cmd == 'insert':
#             train[index] += people
#         elif cmd == 'leave':
#             train[index] -= people
#
#     print(train)
#
#
# wagons = int(input())
# train_passangers(wagons)


END_COMMAND = 'End'
ADD_COMMAND = 'add'
INSERT_COMMAND = 'insert'
LEAVE_COMMAND = 'leave'


def process_command(wagons, command, *args):
    if command == END_COMMAND:
        print(wagons)
        return wagons, False

    if command == ADD_COMMAND:
        wagons[-1] += args[0]
    elif command == INSERT_COMMAND:
        index, people = args
        wagons[index] += people
    elif command == LEAVE_COMMAND:
        index, people = args
        wagons[index] -= people

    return wagons, True


def main():
    wagons = [0] * int(input())

    while True:
        command_input = input().split()
        command = command_input[0]
        args = list(map(int, command_input[1:]))

        wagons, continue_processing = process_command(wagons, command, *args)

        if not continue_processing:
            break


if __name__ == '__main__':
    main()

