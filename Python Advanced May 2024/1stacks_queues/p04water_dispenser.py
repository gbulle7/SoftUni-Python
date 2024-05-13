from collections import deque

quantity = int(input())
name = input()
people = deque()

while name != "Start":
    people.append(name)
    name = input()

command = input()

while command != "End":
    command = command.split()
    if command[0].isnumeric():
        get_water = int(command[0])
        current_person = people.popleft()
        if get_water <= quantity:
            quantity -= get_water
            print(f"{current_person} got water")
        else:
            print(f"{current_person} must wait")
    elif command[0] == "refill":
        fill_water = int(command[1])
        quantity += fill_water
    command = input()

print(f"{quantity} liters left")