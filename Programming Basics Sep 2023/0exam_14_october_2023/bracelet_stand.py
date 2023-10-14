pocket_money_daily = float(input())
earned_money_daily = float(input())
expenses_total = float(input())
gift_price = float(input())

pocket_money_total = 5 * pocket_money_daily
earned_money_total = 5 * earned_money_daily
available_money = pocket_money_total + earned_money_total - expenses_total

if available_money >= gift_price:
    print(f"Profit: {available_money:.2f} BGN, the gift has been purchased.")
else:
    needed_money = gift_price - available_money
    print(f"Insufficient money: {needed_money:.2f} BGN.")