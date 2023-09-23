rest_days = int(input())
working_days = 365 - rest_days
play_working_days = working_days * 63
play_rest_days = rest_days * 127
total_play_time = play_working_days + play_rest_days
difference = abs(30000 - total_play_time)
hours = difference // 60
minutes = difference % 60
if total_play_time >= 30000:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
