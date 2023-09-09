vacation_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
puzzles_price = puzzles * 2.60
dolls_price = dolls * 3
bears_price = bears * 4.1
minions_price = minions * 8.2
trucks_price = trucks * 2
total_price = puzzles_price + dolls_price + bears_price + minions_price + trucks_price
number_toys = puzzles + dolls + bears + minions + trucks
if number_toys >= 50:
    total_price *= 0.75  # 25% discount
rent = total_price * 0.1
remaining_money = total_price - rent
difference = abs(remaining_money - vacation_price)
if remaining_money >= vacation_price:
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')
