country = input()
device = input()

difficulty = 0
execution = 0

if country == 'Russia':
    if device == 'ribbon':
        difficulty = 9.1
        execution = 9.4
    elif device == 'hoop':
        difficulty = 9.3
        execution = 9.8
    elif device == 'rope':
        difficulty = 9.6
        execution = 9.0
elif country == 'Bulgaria':
    if device == 'ribbon':
        difficulty = 9.6
        execution = 9.4
    elif device == 'hoop':
        difficulty = 9.55
        execution = 9.75
    elif device == 'rope':
        difficulty = 9.5
        execution = 9.4
elif country == 'Italy':
    if device == 'ribbon':
        difficulty = 9.2
        execution = 9.5
    elif device == 'hoop':
        difficulty = 9.45
        execution = 9.35
    elif device == 'rope':
        difficulty = 9.7
        execution = 9.15

total_points = difficulty + execution
percent_from_maximum = 100 - total_points * 5  # 1 - total_points / 20%

print(f'The team of {country} get {total_points:.3f} on {device}.')
print(f'{percent_from_maximum:.2f}%')