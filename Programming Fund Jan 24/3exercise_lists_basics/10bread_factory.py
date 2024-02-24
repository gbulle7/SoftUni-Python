events = input().split('|')
total_energy = 100
total_coins = 100

for current_event in events:
    event = current_event.split('-')
    event_type, event_value = event[0], int(event[1])

    if event_type == 'rest':
        energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {total_energy}.')

    elif event_type == 'order':
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f'You earned {event_value} coins.')
        else:
            total_energy += 50
            print(f'You had to rest!')

    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f'You bought {event_type}.')
        else:
            print(f'Closed! Cannot afford {event_type}.')
            break

else:
    print(f'Day completed!'
          f'\nCoins: {total_coins}'
          f'\nEnergy: {total_energy}')
