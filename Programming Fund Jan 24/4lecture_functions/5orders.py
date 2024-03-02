def calculate_price(product, quantity):
    value = None
    if product == 'coffee':
        value = 1.5
        # return f'{1.50 * quantity:.2f}'
    elif product == 'water':
        value = 1
        # return f'{1.00 * quantity:.2f}'
    elif product == 'coke':
        value = 1.4
        # return f'{1.40 * quantity:.2f}'
    elif product == 'snacks':
        value = 2
        # return f'{2.00 * quantity:.2f}'
    return quantity * value


item = input()
number = int(input())
total_price = calculate_price(item, number)
print(f'{total_price:.2f}')
# print(total_price)
