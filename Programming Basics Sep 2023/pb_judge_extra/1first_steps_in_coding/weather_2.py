weather = float(input())
if 26 <= weather <= 35:
    print('Hot')
elif 20.1 <= weather <= 25.9:
    print('Warm')
elif 15 <= weather <= 20:
    print('Mild')
elif 12 <= weather <= 14.9:
    print('Cool')
elif 5 <= weather <= 11.9:
    print('Cold')
else:
    print('unknown')
