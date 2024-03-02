# 1

energy = int(input())
still_have_energy = True
won_battles = 0
command = input()
while command != "End of battle":
    current_distance = int(command)
    if energy - current_distance < 0:  # Not enough energy
        still_have_energy = False
        break
    energy -= current_distance
    won_battles += 1
    if won_battles % 3 == 0:
        energy += won_battles
    command = input()
if still_have_energy:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")

# 2

array = [int(number) for number in input().split()]
command = input().split()
while command[0] != "end":
    action = command[0]
    if action == "swap":
        first_index, second_index = int(command[1]), int(command[2])
        array[first_index], array[second_index] = \
            array[second_index], array[first_index]
    elif action == "multiply":
        first_index, second_index = int(command[1]), int(command[2])
        array[first_index] *= array[second_index]
    elif action == "decrease":
        array = [number - 1 for number in array]
    command = input().split()
# print(", ".join(str(number) for number in array))
print(*array, sep=", ")

# 3

inventory = input().split(", ")
command = input().split(" - ")
while command[0] != "Craft!":
    action = command[0]
    item = command[1]
    if action == "Collect":
        if item not in inventory:
            inventory.append(item)
    elif action == "Drop":
        if item in inventory:
            inventory.remove(item)
    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in inventory:
            old_item_index = inventory.index(old_item)
            inventory.insert(old_item_index + 1, new_item)
    elif action == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)
    command = input().split(" - ")
# print(", ".join(inventory))
print(*inventory, sep=", ")