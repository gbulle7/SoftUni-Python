materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
enough_material = False

while not enough_material:
    stuff = input().split()
    for element in range(0, len(stuff), 2):
        item_name = stuff[element + 1].lower()
        item_quantity = int(stuff[element])

        if item_name in materials:
            materials[item_name] += item_quantity
        elif item_name in junk:
            junk[item_name] += item_quantity
        else:
            junk[item_name] = item_quantity

        for material, quantity in materials.items():
            if quantity >= 250:
                enough_material = material
                materials[material] -= 250
                break
        if enough_material:
            break

if enough_material == 'shards':
    legendary_item = 'Shadowmourne'
elif enough_material == 'fragments':
    legendary_item = 'Valanyr'
else:
    legendary_item = 'Dragonwrath'

print(f'{legendary_item} obtained!')

for key, value in materials.items():
    print(f'{key}: {value}')

for key, value in junk.items():
    print(f'{key}: {value}')


# items = {"shards": 0, "fragments": 0, "motes": 0}
# current_items = input().split()
# obtained = False
# while not obtained:
#     for index in range(0, len(current_items), 2):
#         value = int(current_items[index])
#         key = current_items[index + 1].lower()
#         if key not in items.keys():
#             items[key] = 0
#         items[key] += value
#         if items["shards"] >= 250:
#             print(f"Shadowmourne obtained!")
#             items["shards"] -= 250
#             obtained = True
#         elif items["fragments"] >= 250:
#             print(f"Valanyr obtained!")
#             items["fragments"] -= 250
#             obtained = True
#         elif items["motes"] >= 250:
#             print(f"Dragonwrath obtained!")
#             items["motes"] -= 250
#             obtained = True
#         if obtained:
#             break
#     if obtained:
#         break
#     current_items = input().split()
# for material, quantity in items.items():
#     print(f"{material}: {quantity}")