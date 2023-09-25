game_rounds = int(input())
total_points = 0
interval1 = 0
interval2 = 0
interval3 = 0
interval4 = 0
interval5 = 0
interval6 = 0

for _ in range(game_rounds):
    current_number = int(input())
    if 0 <= current_number <= 9:
        interval1 += 1
        total_points += 0.2 * current_number
    elif 10 <= current_number <= 19:
        interval2 += 1
        total_points += 0.3 * current_number
    elif 20 <= current_number <= 29:
        interval3 += 1
        total_points += 0.4 * current_number
    elif 30 <= current_number <= 39:
        interval4 += 1
        total_points += 50
    elif 40 <= current_number <= 50:
        interval5 += 1
        total_points += 100
    else:
        interval6 += 1
        total_points /= 2

p1 = interval1 / game_rounds * 100
p2 = interval2 / game_rounds * 100
p3 = interval3 / game_rounds * 100
p4 = interval4 / game_rounds * 100
p5 = interval5 / game_rounds * 100
p6 = interval6 / game_rounds * 100

print(f'{total_points:.2f}')
print(f'From 0 to 9: {p1:.2f}%')
print(f'From 10 to 19: {p2:.2f}%')
print(f'From 20 to 29: {p3:.2f}%')
print(f'From 30 to 39: {p4:.2f}%')
print(f'From 40 to 50: {p5:.2f}%')
print(f'Invalid numbers: {p6:.2f}%')

