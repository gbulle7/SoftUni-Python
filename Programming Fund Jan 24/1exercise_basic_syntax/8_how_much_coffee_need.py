string = input()
total_coffees = 0

while string != 'END':
    if string.upper() == 'CODING' or string.upper() == 'DOG' or string.upper() == 'CAT' or string.upper() == 'MOVIE':
        if string.islower():
            total_coffees += 1
        else:
            total_coffees += 2
    string = input()

if total_coffees > 5:
    print('You need extra sleep')
else:
    print(total_coffees)