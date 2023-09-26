joinery_number = int(input())
joinery_type = input()
delivery_method = input()
price = 0

if joinery_type == '90X130':
    price = 110 * joinery_number
    if joinery_number >= 60:
        price *= 0.92
    elif joinery_number >= 30:
        price *= 0.95
elif joinery_type == '100X150':
    price = 140 * joinery_number
    if joinery_number >= 80:
        price *= 0.9
    elif joinery_number >= 40:
        price *= 0.94
elif joinery_type == '130X180':
    price = 190 * joinery_number
    if joinery_number >= 50:
        price *= 0.88
    elif joinery_number >= 20:
        price *= 0.93
else:
    price = 250 * joinery_number
    if joinery_number >= 50:
        price *= 0.86
    elif joinery_number >= 25:
        price *= 0.91

if delivery_method == 'With delivery':
    price += 60

if joinery_number >= 99:
    price *= 0.96

if joinery_number <= 10:
    print('Invalid order')
else:
    print(f'{price:.2f} BGN')