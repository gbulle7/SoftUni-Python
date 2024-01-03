budget = int(input())

while budget >= 0:
    command = input()
    if command == 'End':
        print('You bought everything needed.')
        break
    budget -= int(command)
else:
    print('You went in overdraft!')
