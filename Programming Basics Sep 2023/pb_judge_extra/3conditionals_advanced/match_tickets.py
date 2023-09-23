budget = float(input())
category = input()
people = int(input())
price = 0

if 1 <= people <= 4:
    budget *= 0.25
elif 5 <= people <= 9:
    budget *= 0.4
elif 10 <= people <= 24:
    budget *= 0.5
elif 25 <= people <= 49:
    budget *= 0.6
elif people >= 50:
    budget *= 0.75

if category == 'VIP':
    price = 499.99
elif category == 'Normal':
    price = 249.99

price *= people
difference = abs(budget - price)
if budget >= price:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')
