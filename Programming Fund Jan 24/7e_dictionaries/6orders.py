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


# products = {}
#
# while True:
#     command = input()
#
#     if command == 'buy':
#         break
#
#     name, price, quantity = command.split()
#     price = float(price)
#     quantity = int(quantity)
#
#     if name not in products:
#         products[name] = {'price': price, 'quantity': quantity}
#     else:
#         products[name]['quantity'] += quantity
#
#         if products[name]['price'] != price:
#             products[name]['price'] = price
#
#
# for name, info in products.items():
#     total_price = info['price'] * info['quantity']
#     print(f'{name} -> {total_price:.2f}')



# class Product:
#     def __init__(self, price, quantity):
#         self.price = price
#         self.quantity = quantity
#
#     def update_quantity(self, quantity):
#         self.quantity += quantity
#
#     def update_price(self, price):
#         if self.price != price:
#             self.price = price
#
#
#
# products = {}
#
# while True:
#     command = input()
#
#     if command == 'buy':
#         break
#
#     name, price, quantity = command.split()
#     price = float(price)
#     quantity = int(quantity)
#
#     if name not in products:
#         products[name] = Product(price, quantity)
#     else:
#         products[name].update_quantity(quantity)
#         products[name].update_price(price)
#
#
# for name, product in products.items():
#     total_price = product.price * product.quantity
#     print(f'{name} -> {total_price:.2f}')


# products = {}
# command = input().split()
# while command[0] != "buy":
#     product_name, price, quantity = command[0], float(command[1]), int(command[2])
#     if product_name not in products.keys():
#         products[product_name] = [price, quantity]
#     else:
#         products[product_name][0] = price
#         products[product_name][1] += quantity
#     command = input().split()
# for key, value in products.items():
#     total_price = value[0] * value[1]
#     print(f"{key} -> {total_price:.2f}")
