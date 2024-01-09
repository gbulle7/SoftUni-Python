# lost_fights = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
#
# expenses = 0
# shield_counter = 0
#
# for fight in range(1, lost_fights + 1):
#     if fight % 2 == 0:
#         expenses += helmet_price
#     if fight % 3 == 0:
#         expenses += sword_price
#     if fight % 2 == 0 and fight % 3 == 0:
#         expenses += shield_price
#         shield_counter += 1
#         if shield_counter % 2 == 0:
#             expenses += armor_price
#
# print(f'Gladiator expenses: {expenses:.2f} aureus')

lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_broken = lost_fights // 2
sword_broken = lost_fights // 3
shield_broken = lost_fights // (2*3)
armor_broken = shield_broken // 2

expenses = helmet_broken * helmet_price + sword_broken * sword_price \
           + shield_broken * shield_price + armor_broken * armor_price
print(f'Gladiator expenses: {expenses:.2f} aureus')