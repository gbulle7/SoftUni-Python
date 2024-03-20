stock_line = input().split()
stock = {}

for index in range(0, len(stock_line), 2):
    key = stock_line[index]
    value = stock_line[index + 1]
    stock[key] = int(value)

products = input().split()

for product in products:    # for product in products.keys()
    if product in stock:
        output = f'We have {stock[product]} of {product} left'
    else:
        output = f"Sorry, we don't have {product}"
    print(output)


# def string_dict(elements):
#     elements = elements.split()
#     stock = {}
#     for index in range(0, len(elements), 2):
#         key = elements[index]
#         value = elements[index + 1]
#         stock[key] = int(value)
#     return stock
#
#
# def search_product(items, stock):
#     items = items.split()
#     for item in items:  # for product in products.keys()
#         if item in stock:
#             output = f'We have {stock[item]} of {item} left'
#         else:
#             output = f"Sorry, we don't have {item}"
#         print(output)
#
#
# stock_line = input()
# products = input()
#
# stocks = string_dict(stock_line)
# search_product(products, stocks)
