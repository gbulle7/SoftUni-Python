price_bag_20kg = float(input())
bag_weight = float(input())
days_to_flight = int(input())
bags_number = int(input())
price_bag = 0
if bag_weight < 10:
    price_bag = price_bag_20kg * 0.2
elif bag_weight <= 20:
    price_bag = price_bag_20kg * 0.5
else:
    price_bag = price_bag_20kg

if days_to_flight > 30:
    price_bag *= 1.1
elif days_to_flight >= 7:
    price_bag *= 1.15
else:
    price_bag *= 1.4

total_price = price_bag * bags_number
print(f'The total price of bags is: {total_price:.2f} lv.')