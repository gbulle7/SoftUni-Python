annual_fee = int(input())
shoes = annual_fee - annual_fee * 0.4
kit = shoes - shoes * 0.2
ball = kit * 1/4
accessories = ball * 1/5
total_cost = annual_fee + shoes + kit + ball + accessories
print(total_cost)