lines = int(input())

tank_capacity = 255
tank_filled = 0

for _ in range(lines):
    pour = int(input())
    if pour + tank_filled <= 255:
        tank_filled += pour
    else:
        print(f'Insufficient capacity!')

print(tank_filled)
