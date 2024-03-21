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
