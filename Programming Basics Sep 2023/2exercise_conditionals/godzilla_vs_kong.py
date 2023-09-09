budget = float(input())
number_of_actors = int(input())
price_clothes = float(input())
decor = budget * 0.1
if number_of_actors > 150:
    price_clothes = price_clothes - 0.1 * price_clothes
if price_clothes * number_of_actors + decor > budget:
    print('Not enough money!'
          f'\nWingard needs {(price_clothes * number_of_actors + decor - budget):.2f} leva more.')
else:
    print(f'Action!'
          f'\nWingard starts filming with {(budget - price_clothes * number_of_actors - decor):.2f} leva left.')
