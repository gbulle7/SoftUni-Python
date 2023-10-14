days = int(input())
rakia_total = 0
degrees_total = 0

for day in range(days):
    quantity_rakia = float(input())
    rakia_degree = float(input())
    degree_liter = quantity_rakia * rakia_degree
    degrees_total += degree_liter
    rakia_total += quantity_rakia
average_degrees = degrees_total / rakia_total

print(f"Liter: {rakia_total:.2f}")
print(f"Degrees: {average_degrees:.2f}")
if average_degrees < 38:
    print(f"Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print(f"Super!")
elif average_degrees > 42:
    print(f"Dilution with distilled water!")
