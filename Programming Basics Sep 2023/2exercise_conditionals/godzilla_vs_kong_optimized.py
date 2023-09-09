budget = float(input())
number_of_actors = int(input())
price_clothes = float(input())
decor = budget * 0.1
total_price_clothes = number_of_actors * price_clothes
if number_of_actors > 150:
    total_price_clothes *= 0.9  # total_price_clothes = total_price_clothes - total_price_clothes * 0.1
total_price = total_price_clothes + decor
difference = abs(budget - total_price)
if total_price > budget:
    print(f'Not enough money!'
          f'\nWingard needs {difference:.2f} leva more.')
else:
    print(f'Action!'
          f'\nWingard starts filming with {difference:.2f} leva left.')
