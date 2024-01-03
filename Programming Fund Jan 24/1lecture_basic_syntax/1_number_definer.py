number = float(input())
output = ''

if number == 0:
    output = 'zero'
elif number < 0:
    output = 'negative'
elif number > 0:
    output = 'positive'
if 0 < abs(number) < 1:
    print('small ' + output)
elif abs(number) > 1000000:
    print('large ' + output)
else:
    print(output)
