decorations = int(input())
days_until_christmas = int(input())
ornament_price = 2
treeskirt_price = 5
garland_price = 3
lights_price = 15
days_counter = 0
money_needed = 0
total_points = 0

while days_until_christmas > 0:
    days_counter += 1
    if days_counter % 11 == 0:
        decorations += 2
    if days_counter % 2 == 0:
        money_needed += ornament_price * decorations
        total_points += 5
    if days_counter % 3 == 0:
        money_needed += decorations * (treeskirt_price + garland_price)
        total_points += 13
    if days_counter % 15 == 0:
        total_points += 30
    if days_counter % 5 == 0:
        money_needed += lights_price * decorations
        total_points += 17
    if days_counter % 10 == 0:
        total_points -= 20
        money_needed += treeskirt_price + garland_price + lights_price
    if days_until_christmas == 1 and days_counter % 10 == 0:
        total_points -= 30
    days_until_christmas -= 1

print(f'Total cost: {money_needed}')
print(f'Total spirit: {total_points}')

# decorations = int(input())
# days_until_christmas = int(input())
# ornament_price = 2
# treeskirt_price = 5
# garland_price = 3
# lights_price = 15
#
# budget = 0
# total_points = 0
#
# for day in range(1, days_until_christmas + 1):
#     if day % 11 == 0:
#         decorations += 2
#     if day % 2 == 0:
#         budget += ornament_price * decorations
#         total_points += 5
#     if day % 3 == 0:
#         budget += decorations * (treeskirt_price + garland_price)
#         total_points += 13
#     if day % 15 == 0:
#         total_points += 30
#     if day % 5 == 0:
#         budget += lights_price * decorations
#         total_points += 17
#     if day % 10 == 0:
#         total_points -= 20
#         budget += treeskirt_price + garland_price + lights_price
#         if day == days_until_christmas:
#             total_points -= 30
#
# print(f'Total cost: {budget}')
# print(f'Total spirit: {total_points}')