from math import floor, ceil

vineyard_area = int(input())
grape_per_sqmeter = float(input())
needed_wine = int(input())
workers_number = int(input())
used_area = vineyard_area * 0.4
total_grape = grape_per_sqmeter * used_area
total_wine = total_grape / 2.5
difference = abs(total_wine - needed_wine)
if total_wine < needed_wine:
    print(f'It will be a tough winter! More {floor(difference)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {floor(total_wine)} liters.')
    wine_per_person = ceil(difference / workers_number)
    print(f'{ceil(difference)} liters left -> {wine_per_person} liters per person.')
