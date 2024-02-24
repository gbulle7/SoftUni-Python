gifts = input().split()
command = input()

while command != 'No Money':
    gift = command.split()
    state, name = gift[0], gift[1]

    if state == 'OutOfStock' and name in gifts:
        gifts = list(map(lambda lst: lst.replace(name, 'None'),gifts))
        # for index, present in enumerate(gifts):
        #     if present == name:
        #         gifts[index] = 'None'
    elif state == 'Required':
        if int(gift[2]) in range(len(gifts)):
            gifts[int(gift[2])] = name
    elif state == 'JustInCase':
        gifts[-1] = name
    command = input()

while 'None' in gifts:
    gifts.remove('None')

for element in gifts:
    print(element, end=' ')
