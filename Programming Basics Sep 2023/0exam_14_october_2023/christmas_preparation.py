paper_rolls = int(input())
cloth_rolls = int(input())
glue_liters = float(input())
discount = int(input())
paper_price = paper_rolls * 5.8
cloth_price = cloth_rolls * 7.2
glue_price = glue_liters * 1.2

total_price = paper_price + cloth_price + glue_price
discounted_price = total_price * (1 - discount * 0.01)

print(f'{discounted_price:.3f}')