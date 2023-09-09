hour = int(input())
minutes = int(input())
plus_fifteen = minutes + 15
if plus_fifteen >= 60:
    hour += 1
    plus_fifteen -= 60
if hour >= 24:  # hour > 23
    hour = 24  # hour = 0
print(f'{hour}:{plus_fifteen:02d}')
