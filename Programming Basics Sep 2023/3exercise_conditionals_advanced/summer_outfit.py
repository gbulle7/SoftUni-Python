temperature = int(input())
day_time = input()
outfit = ''
shoes = ''

if day_time == 'Morning':
    if 10 <= temperature <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < temperature <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temperature >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif day_time == 'Afternoon':
    if 10 <= temperature <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < temperature <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif temperature >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
elif day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")