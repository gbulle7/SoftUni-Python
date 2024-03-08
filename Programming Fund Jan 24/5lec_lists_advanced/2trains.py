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

def train_passangers(wgons):
    train = [0] * wgons

    while True:
        command = input().split()
        if command[0] == 'End':
            break
        cmd = command[0]
        index = int(command[1])
        people = int(command[-1])

        if cmd == 'add':
            train[-1] += people
        elif cmd == 'insert':
            train[index] += people
        elif cmd == 'leave':
            train[index] -= people

    print(train)


wagons = int(input())
train_passangers(wagons)

