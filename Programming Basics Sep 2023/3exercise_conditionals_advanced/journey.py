budget = float(input())
season = input()
location = ''
resort = ''
price = budget

if price <= 100:
    location = 'Bulgaria'
    if season == 'summer':
        resort = 'Camp'
        price *= 0.3
    else:
        resort = 'Hotel'
        price *= 0.7
elif price <= 1000:
    location = 'Balkans'
    if season == 'summer':
        resort = 'Camp'
        price *= 0.4
    else:
        resort = 'Hotel'
        price *= 0.8
else:
    location = 'Europe'
    resort = 'Hotel'
    price *= 0.9

print(f'Somewhere in {location} '
      f'\n{resort} - {price:.2f}')
