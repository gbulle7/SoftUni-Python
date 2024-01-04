number_orders = int(input())
total_price = 0

for _ in range(number_orders):
    price_capsule = float(input())
    days = int(input())
    capsule_day = int(input())
    price_order = price_capsule * days * capsule_day
    if price_capsule < 0.01 or price_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsule_day < 1 or capsule_day > 2000:
        continue
    total_price += price_order
    print(f'The price for the coffee is: ${price_order:.2f}')
print(f'Total: ${total_price:.2f}')
