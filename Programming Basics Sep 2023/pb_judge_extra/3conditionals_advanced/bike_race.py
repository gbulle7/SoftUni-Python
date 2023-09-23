juniors = int(input())
seniors = int(input())
race_type = input()
price_juniors = 0
price_seniors = 0

if race_type == 'trail':
    price_juniors = 5.5
    price_seniors = 7
elif race_type == 'cross-country':
    price_juniors = 8
    price_seniors = 9.5
    if juniors + seniors >= 50:
        price_juniors *= 0.75
        price_seniors *= 0.75
elif race_type == 'downhill':
    price_juniors = 12.25
    price_seniors = 13.75
elif race_type == 'road':
    price_juniors = 20
    price_seniors = 21.5

total_sum = price_juniors * juniors + price_seniors * seniors
total_sum *= 0.95
print(f'{total_sum:.2f}')