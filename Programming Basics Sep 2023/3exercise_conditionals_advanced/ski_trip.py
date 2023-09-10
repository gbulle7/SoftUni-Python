days = int(input())
place_type = input()
review = input()
nights = days - 1
price = 0

if place_type == 'room for one person':
    price = nights * 18
elif place_type == 'apartment':
    price = nights * 25
    if nights < 10:
        price *= 0.7
    elif nights <= 15:
        price *= 0.65
    else:
        price *= 0.5
elif place_type == 'president apartment':
    price = nights * 35
    if nights < 10:
        price *= 0.9
    elif nights <= 15:
        price *= 0.85
    else:
        price *= 0.80

if review == 'positive':
    price *= 1.25
else:
    price *= 0.9
print(f'{price:.2f}')
