products = {}

while True:
    buy = input()
    if buy == 'buy':
        break

    name, price, quantity = buy.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {price: quantity}
    else:
        old_cost = products[name].popitem()
        products[name][price] = old_cost[1] + quantity

for product, cost in products.items():
    for price, quantity in cost.items():
        total_product_price = price * quantity
        print(f'{product} -> {total_product_price:.2f}')
