from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

points = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'}
gifts = {}

while materials and magic:
    total_magic = materials[-1] * magic[0]
    if total_magic in points:
        new_gift = points[total_magic]
        if new_gift not in gifts:
            gifts[new_gift] = 0
        gifts[new_gift] += 1
        materials.pop()
        magic.popleft()
    elif total_magic > 0:
        magic.popleft()
        materials[-1] += 15
    elif total_magic < 0:
        new_materials = materials[-1] + magic[0]
        materials.pop()
        magic.popleft()
        materials.append(new_materials)
    else:
        if materials[-1] == 0:
            materials.pop()
        if magic[0] == 0:
            magic.popleft()

# while materials and magic_levels:
#     material = materials.pop()
#     magic = magic_levels.popleft()
#     level = material * magic
#     if level in magic_required:
#         current_present = magic_required[level]
#         if current_present not in presents:
#             presents[current_present] = 0
#         presents[current_present] += 1
#     else:
#         if level < 0:
#             materials.append(material + magic)
#         elif level > 0:
#             materials.append(material + 15)
#         else:
#             if magic == 0 and material == 0:
#                 continue
#             elif magic == 0:
#                 materials.append(material)
#             else:
#                 magic_levels.appendleft(magic)

if ('Doll' in gifts and 'Wooden train' in gifts) or ('Teddy bear' in gifts and 'Bicycle' in gifts):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")    # materials[::-1]
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")
print(*sorted([f"{key}: {value}" for key, value in gifts.items()]), sep='\n')
