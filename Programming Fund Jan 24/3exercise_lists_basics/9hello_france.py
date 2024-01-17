collection = input().split('|')
budget = float(input())

new_prices = []
profit = 0

for item in collection:
    type_item, value_item = item.split('->')
    value_item = float(value_item)
    purchasable = (
        (type_item == 'Clothes' and value_item <= 50.0) or
        (type_item == 'Shoes' and value_item <= 35) or
        (type_item == 'Accessories' and value_item <= 20.5)
    )

    if purchasable:
        if budget >= value_item:
            budget -= value_item
            mark_up_value = value_item * 1.4
            profit += mark_up_value - value_item
            new_prices.append(mark_up_value)

string_prices = ''
for element in new_prices:
    string_prices += f'{element:.2f} '
print(string_prices)

print(f'Profit: {profit:.2f}')

if budget + sum(new_prices) >= 150:
    print('Hello, France!')
else:
    print(f'Not enough money.')

