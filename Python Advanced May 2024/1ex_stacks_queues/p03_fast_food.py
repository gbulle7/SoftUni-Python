from collections import deque

quantity = int(input())
# orders = [int(x) for x in input().split()]
# remaining_orders = deque(orders)
# # orders = list(map(int, input().split()))
# # orders = list(map(lambda x: int(x), input().split()))
# orders_complete = False
# for order in orders:
#     if quantity - order >= 0:
#         quantity -= remaining_orders.popleft()
#     else:
#         break
# else:
#     orders_complete = True
#
# print(max(orders))
# if orders_complete:
#     print("Orders complete")
# else:
#     print("Orders left:", " ".join(map(str, remaining_orders)))

orders = deque([int(x) for x in input().split()])
print(max(orders))
while orders and orders[0] <= quantity:
    quantity -= orders.popleft()
if orders:
    print("Orders left:", *orders)
else:
    print("Orders complete")
