number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegan_menu = int(input())
chicken_price = number_chicken_menu * 10.35
fish_price = number_fish_menu * 12.40
vegan_price = number_vegan_menu * 8.15
main_menu_price = chicken_price + fish_price + vegan_price
dessert_price = main_menu_price * 0.2
delivery_price = 2.5
total_price = main_menu_price + dessert_price + delivery_price
print(total_price)