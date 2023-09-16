# method 1 with while loop
change = float(input())
change = int(change * 100)  # transform levs into cents, example: float(1.23) to int(123)
coins_counter = 0

while change > 0:
    if change >= 200:
        coins_counter += 1
        change -= 200
    elif change >= 100:
        coins_counter += 1
        change -= 100
    elif change >= 50:
        coins_counter += 1
        change -= 50
    elif change >= 20:
        coins_counter += 1
        change -= 20
    elif change >= 10:
        coins_counter += 1
        change -= 10
    elif change >= 5:
        coins_counter += 1
        change -= 5
    elif change >= 2:
        coins_counter += 1
        change -= 2
    elif change >= 1:
        coins_counter += 1
        change -= 1
print(coins_counter)

# method 2 with // and %, without loop
# change = float(input())
# change = int(change * 100)  # transform levs into cents, example: float(1.23) to int(123)
# coins_counter = 0
# coins_counter += change // 200
# change %= 200
# coins_counter += change // 100
# change %= 100
# coins_counter += change // 50
# change %= 50
# coins_counter += change // 20
# change %= 20
# coins_counter += change // 10
# change %= 10
# coins_counter += change // 5
# change %= 5
# coins_counter += change // 2
# change %= 2
# coins_counter += change // 1
# change %= 1
# print(coins_counter)

# method 3
# change = float(input())
# coins_counter = 0
#
# while change > 0:
#     if change >= 2:
#         change -= 2
#     elif change >= 1:
#         change -= 1
#     elif change >= 0.50:
#         change -= 0.50
#     elif change >= 0.20:
#         change -= 0.20
#     elif change >= 0.10:
#         change -= 0.10
#     elif change >= 0.05:
#         change -= 0.05
#     elif change >= 0.02:
#         change -= 0.02
#     elif change >= 0.01:
#         change -= 0.01
#
#     change = round(change, 2)  # rounding float to 2nd digit
#     coins_counter += 1
#
# print(coins_counter)