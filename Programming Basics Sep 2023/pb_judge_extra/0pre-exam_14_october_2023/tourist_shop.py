budget = float(input())
product_name = input()
counter = 0
total_price = 0

while product_name != 'Stop':
    counter += 1
    product_price = float(input())
    if counter % 3 == 0:
        product_price *= 0.5
    total_price += product_price
    if total_price > budget:
        needed_money = total_price - budget
        print(f"You don't have enough money!")
        print(f"You need {needed_money:.2f} leva!")
        break
    product_name = input()
else:
    print(f'You bought {counter} products for {total_price:.2f} leva.')