season = input()
distance_per_month = float(input())
wage_per_km = 0

if distance_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        wage_per_km = 0.75
    elif season == 'Summer':
        wage_per_km = 0.9
    elif season == 'Winter':
        wage_per_km = 1.05
elif distance_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        wage_per_km = 0.95
    elif season == 'Summer':
        wage_per_km = 1.1
    elif season == 'Winter':
        wage_per_km = 1.25
elif distance_per_month <= 20000:
    wage_per_km = 1.45

wage_per_km *= 0.9  # after 10% taxes
salary = distance_per_month * wage_per_km * 4   # 4 period_months per season
print(f'{salary:.2f}')
