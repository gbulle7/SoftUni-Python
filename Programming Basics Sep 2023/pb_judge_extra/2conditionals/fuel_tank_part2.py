fuel_type = input()
fuel_quantity = float(input())
discount_card = input()
gasoline = 2.22
diesel = 2.33
gas = 0.93
if discount_card == 'Yes':
    gasoline -= 0.18
    diesel -= 0.12
    gas -= 0.08
if fuel_type == 'Gasoline':
    total_fuel_price = gasoline * fuel_quantity
elif fuel_type == 'Diesel':
    total_fuel_price = diesel * fuel_quantity
else:
    total_fuel_price = gas * fuel_quantity
if 20 <= fuel_quantity <= 25:
    total_fuel_price *= 0.92
elif fuel_quantity > 25:
    total_fuel_price *= 0.90
print(f'{total_fuel_price:.2f} lv.')
