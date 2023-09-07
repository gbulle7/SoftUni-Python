nylon = int(input())
paint = int(input())
thinner = int(input())
time = int(input())
nylon_price = 1.5
paint_price = 14.5
thinner_price = 5
additional_materials = 0.1 * paint * paint_price + 2 * nylon_price + 0.40
total_price_of_materials = nylon * nylon_price + paint * paint_price \
                           + thinner * thinner_price + additional_materials
work_cost = total_price_of_materials * 0.3 * time
total_cost = total_price_of_materials + work_cost
print(total_cost)