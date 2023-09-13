age = int(input())
washmachine_price = float(input())
toy_price = int(input())
toy_number = 0
total_sum = 0
money_gift = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        money_gift += 10
        total_sum += money_gift - 1
    else:
        toy_number += 1

all_toys_price = toy_number * toy_price
total_sum += all_toys_price
difference = abs(total_sum - washmachine_price)
if total_sum >= washmachine_price:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')