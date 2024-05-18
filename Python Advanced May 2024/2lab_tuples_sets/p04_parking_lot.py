n = int(input())
parking_lot = set()
for _ in range(n):
    direction, plate = input().split(', ')
    if direction == "IN":
        parking_lot.add(plate)
    elif direction == "OUT" and plate in parking_lot:
        parking_lot.remove(plate)
if parking_lot:
    {print(car_plate) for car_plate in parking_lot}
else:
    print('Parking Lot is Empty')
