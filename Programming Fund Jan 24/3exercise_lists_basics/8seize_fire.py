fire_cells = input().split('#')
water = int(input())
extinguished_cells = []
total_fire = 0
total_effort = 0

for fire_cell in fire_cells:
    current_cell = fire_cell.split(' = ')
    fire_type, cell_value = current_cell[0], int(current_cell[1])
    valid_cell = False
    if fire_type == 'High' and 81 <= cell_value <= 125:
        valid_cell = True
    elif fire_type == 'Medium' and 51 <= cell_value <= 80:
        valid_cell = True
    elif fire_type == 'Low' and 1 <= cell_value <= 50:
        valid_cell = True

    if valid_cell:
        if water >= cell_value:
            water -= cell_value
            extinguished_cells.append(cell_value)
            total_effort += cell_value * 0.25
            total_fire += cell_value

print('Cells:')
for cell in extinguished_cells:
    print(f' - {cell}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')
