age = float(input())
gender = input()
if age >= 16:
    if gender == 'm':
        print('Mr.')
    else:   # elif gender == 'f'
        print('Ms.')
else:
    if gender == 'm':
        print('Master')
    else:   # elif gender == 'f'
        print('Miss')
