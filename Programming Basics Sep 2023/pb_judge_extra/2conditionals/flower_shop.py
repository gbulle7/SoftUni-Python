from math import floor, ceil

magnolias = int(input())
hyacinthes = int(input())
roses = int(input())
cactuses = int(input())
gift_price = float(input())
magnolias_price = magnolias * 3.25
hyacinthes_price = hyacinthes * 4
roses_price = roses * 3.5
cactuses_price = cactuses * 8
total_cost = (magnolias_price + hyacinthes_price + roses_price + cactuses_price) * 0.95  # 5% for taxes
difference = abs(total_cost - gift_price)
if total_cost >= gift_price:
    print(f'She is left with {floor(difference)} leva.')
else:
    print(f'She will have to borrow {ceil(difference)} leva.')
