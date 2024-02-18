vehicles = input().split('>>')

total_revenue = 0

for vehicle in vehicles:
    final_tax = 0
    each_vehicle = vehicle.split()
    vehicle_type, years_tax, mileage = each_vehicle[0], each_vehicle[1], each_vehicle[2]
    years_tax = int(years_tax)
    mileage = int(mileage)
    if vehicle_type == 'family':
        initial_tax = 50
        initial_tax -= 5 * years_tax
        final_tax = initial_tax + 12 * (mileage // 3000)
    elif vehicle_type == 'heavyDuty':
        initial_tax = 80
        initial_tax -= 8 * years_tax
        final_tax = initial_tax + 14 * (mileage // 9000)
    elif vehicle_type == 'sports':
        initial_tax = 100
        initial_tax -= 9 * years_tax
        final_tax = initial_tax + 18 * (mileage // 2000)
    else:
        print('Invalid car type.')
        continue
    print(f'A {vehicle_type} car will pay {final_tax:.2f} euros in taxes.')

    total_revenue += final_tax

print(f'The National Revenue Agency will collect {total_revenue:.2f} euros in taxes.')





