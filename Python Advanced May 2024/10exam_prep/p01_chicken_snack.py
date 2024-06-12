from collections import deque

money = [int(x) for x in input().split()]
prices = deque([int(x) for x in input().split()])
# money = list(map(int, input().split()))
# prices = deque(map(int, input().split()))

food_count = 0

while money and prices:
    curr_money = money.pop()
    curr_food = prices.popleft()
    if curr_money == curr_food:
        food_count += 1
    elif curr_money > curr_food:
        food_count += 1
        difference = curr_money - curr_food
        if money:
            money[-1] += difference

if food_count == 0:
    msg = f'Henry remained hungry. He will try next weekend again.'
elif food_count == 1:
    msg = f'Henry ate: {food_count} food.'
elif food_count < 4:
    msg = f'Henry ate: {food_count} foods.'
else:
    msg = f'Gluttony of the day! Henry ate {food_count} foods.'

print(msg)

# if count >= 4:
#     print(f"Gluttony of the day! Henry ate {count} foods.")
# elif count == 0:
#     print("Henry remained hungry. He will try next weekend again.")
# else:
#     print(f"Henry ate: {count} food{'s' if count != 1 else ''}.")
