from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])
wasted_water = 0

while cups and bottles:
    cups[0] -= bottles[-1]
    if cups[0] <= 0:
        wasted_water -= cups[0]
        cups.popleft()
    bottles.pop()
if bottles:
    print(f"Bottles:", *bottles)
elif cups:
    print(f"Cups:", *cups)
print(f"Wasted litters of water: {wasted_water}")
