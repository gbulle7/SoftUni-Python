budget = float(input())
season = input()
category = ''
car_type = ''
price = 0

if budget <= 100:
    category = 'Economy class'
    if season == 'Summer':
        car_type = 'Cabrio'
        price = budget * 0.35
    elif season == 'Winter':
        car_type = 'Jeep'
        price = budget * 0.65
elif 100 < budget <= 500:
    category = 'Compact class'
    if season == 'Summer':
        car_type = 'Cabrio'
        price = budget * 0.45
    elif season == 'Winter':
        car_type = 'Jeep'
        price = budget * 0.8
elif budget > 500:
        category = 'Luxury class'
        car_type = 'Jeep'
        price = budget * 0.9

print(category)
print(f'{car_type} - {price:.2f}')
