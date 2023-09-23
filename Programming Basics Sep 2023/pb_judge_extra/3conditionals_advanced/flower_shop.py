chrysants_number = int(input())
roses_number = int(input())
tulips_number = int(input())
season = input()
celebration = input()
price_chrysants = 0
price_roses = 0
price_tulips = 0

if season == 'Spring' or season == 'Summer':
    price_chrysants = 2
    price_roses = 4.1
    price_tulips = 2.5
elif season == 'Autumn' or season == 'Winter':
    price_chrysants = 3.75
    price_roses = 4.5
    price_tulips = 4.15

total_price = price_tulips * tulips_number + price_roses * roses_number + price_chrysants * chrysants_number
if celebration == 'Y':
    total_price *= 1.15

if tulips_number > 7 and season == 'Spring':
    total_price *= 0.95
elif roses_number >= 10 and season == 'Winter':
    total_price *= 0.9

total_flowers = chrysants_number + roses_number + tulips_number
if total_flowers > 20:
    total_price *= 0.8
total_price += 2
print(f'{total_price:.2f}')