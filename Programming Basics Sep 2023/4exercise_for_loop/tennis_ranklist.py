tournaments_number = int(input())
starting_points = int(input())
tournament_points = 0
number_won = 0

for _ in range(tournaments_number):
    position = input()
    if position == 'W':
        tournament_points += 2000
        number_won += 1
    elif position == 'F':
        tournament_points += 1200
    elif position == 'SF':
        tournament_points += 720
total_points = starting_points + tournament_points
average_points = tournament_points // tournaments_number  # == int(t.points/t.number); == floor(t.points/t.number)
win_percentage = number_won / tournaments_number * 100

print(f'Final points: {total_points}')
print(f'Average points: {average_points}')
print(f'{win_percentage:.2f}%')


