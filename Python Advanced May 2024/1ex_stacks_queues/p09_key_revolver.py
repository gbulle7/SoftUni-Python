from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())
current_ammo = barrel_size

while locks and bullets:
    if bullets[-1] > locks[0]:
        print("Ping!")
    else:
        print("Bang!")
        locks.popleft()
    bullets.pop()
    intelligence_value -= bullet_price
    current_ammo -= 1
    if bullets and current_ammo == 0:
        current_ammo = barrel_size
        print("Reloading!")
if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
