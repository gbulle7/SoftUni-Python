# n = int(input())
# parking_lot = set()
# for _ in range(n):
#     direction, plate = input().split(', ')
#     if direction == "IN":
#         parking_lot.add(plate)
#     elif direction == "OUT" and plate in parking_lot:
#         parking_lot.remove(plate)
# if parking_lot:
#     {print(car_plate) for car_plate in parking_lot}
# else:
#     print('Parking Lot is Empty')

def add_car(parking, car_plate):
    parking.add(car_plate)


def remove_car(parking, car_plate):
    if car_plate in parking:
        parking.remove(car_plate)


n = int(input())
parking_lot = set()
mapper = {"IN": add_car, "OUT": remove_car}

for _ in range(n):
    direction, plate = input().split(', ')
    mapper[direction](parking_lot, plate)
if parking_lot:
    print(*parking_lot, sep='\n')
else:
    print('Parking Lot is Empty')
