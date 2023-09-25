cargo_number = int(input())
bus = 0
truck = 0
train = 0
total_weight = 0

for _ in range(cargo_number):
    current_cargo_weight = int(input())
    total_weight += current_cargo_weight
    if current_cargo_weight <= 3:
        bus += current_cargo_weight
    elif current_cargo_weight <= 11:
        truck += current_cargo_weight
    else:
        train += current_cargo_weight

average_price = (bus * 200 + truck * 175 + train * 120) / total_weight
bus_percent = bus / total_weight * 100
truck_percent = truck / total_weight * 100
train_percent = train / total_weight * 100

print(f'{average_price:.2f}')
print(f'{bus_percent:.2f}%')
print(f'{truck_percent:.2f}%')
print(f'{train_percent:.2f}%')
