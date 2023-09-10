flower_type = input()
number_flowers = int(input())
budget = int(input())
price = 0

if flower_type == 'Roses':
    price = 5
    if number_flowers > 80:
        price *= 0.9
elif flower_type == 'Dahlias':
    price = 3.8
    if number_flowers > 90:
        price *= 0.85
elif flower_type == 'Tulips':
    price = 2.8
    if number_flowers > 80:
        price *= 0.85
elif flower_type == 'Narcissus':
    price = 3
    if number_flowers < 120:
        price *= 1.15
elif flower_type == 'Gladiolus':
    price = 2.5
    if number_flowers < 80:
        price *= 1.2

total_price = price * number_flowers
difference = abs(budget - total_price)
if budget >= total_price:
    print(f'Hey, you have a great garden with {number_flowers} {flower_type} and {difference:.2f} leva left.')
else:
    print(f'Not enough money, you need {difference:.2f} leva more.')
