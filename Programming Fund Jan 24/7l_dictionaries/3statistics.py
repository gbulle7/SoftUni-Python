stock = {}

while True:
    product = input().split(': ')
    if product[0] == 'statistics':
        break
    product_name = product[0]
    product_quantity = product[1]
    if product_name not in stock:
        stock[product_name] = 0
    stock[product_name] += int(product_quantity)

print('Products in stock:')
[print(f'- {item}: {quantity}') for item, quantity in stock.items()]
# for product in stock:
#     print(f'- {product}: {stock[product]}')

# for product, quantity in stock.items():
#     print(f'- {product}: {quantity}')
print(f'Total Products: {len(stock)}')
print(f'Total Quantity: {sum(stock.values())}')
