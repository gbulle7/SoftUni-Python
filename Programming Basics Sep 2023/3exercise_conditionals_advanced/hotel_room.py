month = input()
nights = int(input())
studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = 50
    if nights > 14:
        studio_price *= 0.7
    elif nights > 7:
        studio_price *= 0.95
    apartment_price = 65
elif month == 'June' or month == 'September':
    studio_price = 75.2
    if nights > 14:
        studio_price *= 0.8
    apartment_price = 68.7
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77

if nights > 14:
    apartment_price *= 0.9

total_apartment_price = apartment_price * nights
total_studio_price = studio_price * nights

print(f'Apartment: {total_apartment_price:.2f} lv.'
      f'\nStudio: {total_studio_price:.2f} lv.')
