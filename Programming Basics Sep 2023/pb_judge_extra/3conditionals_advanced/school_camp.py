season = input()
group_type = input()
students = int(input())
nights = int(input())
price_per_night = 0
sport = ''

if season == 'Winter':
    if group_type == 'boys' or group_type == 'girls':
        price_per_night = 9.6
    elif group_type == 'mixed':
        price_per_night = 10
elif season == 'Spring':
    if group_type == 'boys' or group_type == 'girls':
        price_per_night = 7.2
    elif group_type == 'mixed':
        price_per_night = 9.5
elif season == 'Summer':
    if group_type == 'boys' or group_type == 'girls':
        price_per_night = 15
    elif group_type == 'mixed':
        price_per_night = 20
total_price = price_per_night * nights * students
if students >= 50:
    total_price *= 0.5
elif students >= 20:
    total_price *= 0.85
elif students >= 10:
    total_price *= 0.95

if group_type == 'girls':
    if season == 'Winter':
        sport = 'Gymnastics'
    elif season == 'Spring':
        sport = 'Athletics'
    elif season == 'Summer':
        sport = 'Volleyball'
elif group_type == 'boys':
    if season == 'Winter':
        sport = 'Judo'
    elif season == 'Spring':
        sport = 'Tennis'
    elif season == 'Summer':
        sport = 'Football'
elif group_type == 'mixed':
    if season == 'Winter':
        sport = 'Ski'
    elif season == 'Spring':
        sport = 'Cycling'
    elif season == 'Summer':
        sport = 'Swimming'
print(f'{sport} {total_price:.2f} lv.')
