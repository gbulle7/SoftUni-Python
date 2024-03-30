import re

command = input()
total_cost = 0
bought_furniture = []
pattern = r'>>([a-zA-Z]+)<<(\d+\.?\d+)!(\d+\b)'

while command != 'Purchase':
    match = re.search(pattern, command)
    if match:
        furniture_name, price, quantity = match.groups()
        # furniture_name = match.group(1)
        # price = match.group(2)
        # quantity = match.group(3)
        bought_furniture.append(furniture_name)
        furniture_price = float(price) * int(quantity)
        total_cost += furniture_price
    command = input()

print('Bought furniture:')
for furniture in bought_furniture:
    print(furniture)
print(f'Total money spend: {total_cost:.2f}')


# import re
#
# main_string = input()
#
# pattern = re.compile(
#     r">>(?P<furniture_name>[A-Za-z]+)<<(?P<price>[0-9]+[.0-9]*)!(?P<quantity>[0-9]+)")
#
# total_money_spend = 0
# print("Bought furniture:")
# while main_string != "Purchase":
#     result = re.finditer(pattern, main_string)
#     for show in result:
#         total_money_spend += float(show["price"]) * float(show["quantity"])
#         print(show["furniture_name"])
#     main_string = input()
#
# print(f"Total money spend: {total_money_spend:.2f}")
