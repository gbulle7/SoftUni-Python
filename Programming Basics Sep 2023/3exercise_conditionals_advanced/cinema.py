screening_type = input()
rows = int(input())
columns = int(input())
total_seats = rows * columns
price = 0

if screening_type == 'Premiere':
    price = 12
elif screening_type == 'Normal':
    price = 7.5
elif screening_type == 'Discount':
    price = 5

revenue = price * total_seats
print(f'{revenue:.2f} leva')
