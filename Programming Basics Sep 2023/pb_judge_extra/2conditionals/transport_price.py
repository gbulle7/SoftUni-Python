distance = int(input())
day_night = input()
taxi = 0.70  # starting fee, excluded day/night price per km
bus = 0.09 * distance
train = 0.06 * distance

if distance >= 100:
    print(f'{train:.2f}')
elif distance < 20:
    if day_night == 'day':
        bonus = 0.79 * distance
    else:
        bonus = 0.90 * distance
    taxi += bonus
    print(f'{taxi:.2f}')
else:
    print(f'{bus:.2f}')
