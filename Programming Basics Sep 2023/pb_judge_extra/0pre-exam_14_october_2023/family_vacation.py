budget = float(input())
nights = int(input())
price_night = float(input())
additional_costs_percent = int(input())

if nights > 7:
    price_night *= 0.95

total_price = price_night * nights
available_money = budget * (1 - additional_costs_percent * 0.01)
difference = f'{abs(available_money - total_price):.2f}'
if available_money >= total_price:
    print(f"Ivanovi will be left with {difference} leva after vacation.")
else:
    print(f"{difference} leva needed.")
