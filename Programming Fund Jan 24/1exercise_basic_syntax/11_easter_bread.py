budget = float(input())
flour_kg_price = float(input())
egg_pack_price = 0.75 * flour_kg_price
milk_l_price = 1.25 * flour_kg_price
number_of_loaves = 0
colored_eggs = 0
current_bread_count = 0
remaining_cash = budget

while True:
    budget -= (egg_pack_price + milk_l_price * 0.25 + flour_kg_price)
    if budget <= 0:
        break
    number_of_loaves += 1
    current_bread_count += 1
    colored_eggs += 3
    if current_bread_count == 3:
        colored_eggs -= number_of_loaves - 2
        current_bread_count = 0
    remaining_cash = budget

print(f'You made {number_of_loaves} loaves of Easter bread! '
      f'Now you have {colored_eggs} eggs and {remaining_cash:.2f}BGN left.')

# budget = float(input())
# price_for_kg_flour = float(input())
# price_for_pack_eggs = price_for_kg_flour * 0.75
# price_for_quart_milk = (price_for_kg_flour * 1.25) / 4
#
# money_needed_for_one_loaf = price_for_kg_flour + price_for_pack_eggs + price_for_quart_milk
#
# loaves = 0
# colored_eggs = 0
#
# while budget >= money_needed_for_one_loaf:
#       loaves += 1
#       budget -= money_needed_for_one_loaf
#       colored_eggs += 3
#       if loaves % 3 == 0:
#             colored_eggs -= loaves - 2
#
# print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs "
#       f"and {budget:.2f}BGN left.")