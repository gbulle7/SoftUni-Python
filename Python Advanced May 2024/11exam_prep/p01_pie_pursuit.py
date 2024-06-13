from collections import deque

contestants = deque(int(x) for x in input().split())
pies = [int(x) for x in input().split()]

while contestants and pies:
    contestant = contestants.popleft()
    pie_size = pies.pop()
    if contestant >= pie_size:
        contestant -= pie_size
        if contestant > 0:
            contestants.append(contestant)

    elif pie_size > contestant:
        pie_size -= contestant
        if pies and pie_size == 1:
            pies[-1] += pie_size
        else:
            pies.append(pie_size)


if not pies and not contestants:
    print('We have a champion!')
elif contestants:
    print(f'We will have to wait for more pies to be baked!')
    print(f"Contestants left: {', '.join(str(x) for x in contestants)}")
elif pies:
    print(f'Our contestants need to rest!')
    print(f"Pies left: {', '.join(str(x) for x in pies)}")
