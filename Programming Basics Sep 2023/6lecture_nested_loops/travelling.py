destination = input()
budget = 0

while destination != 'End':
    price = input()
    while budget < float(price):
        budget += float(input())
    print(f'Going to {destination}!')
    budget = 0
    destination = input()
