from collections import deque

choco = [int(x) for x in input().split(', ')]
cups = deque([int(x) for x in input().split(', ')])
milkshakes = 0

while choco and cups and milkshakes < 5:
    if choco[-1] <= 0 and cups[0] <= 0:
        choco.pop()
        cups.popleft()
        continue
    if choco[-1] <= 0:
        choco.pop()
        continue
    if cups[0] <= 0:
        cups.popleft()
        continue
    if choco[-1] == cups[0]:
        milkshakes += 1
        choco.pop()
        cups.popleft()
    else:
        choco[-1] -= 5
        cups.rotate(-1)

if milkshakes >= 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')
print(f"Chocolate: {', '.join([str(x) for x in choco]) if choco else 'empty'}")
print(f"Milk: {', '.join([str(x) for x in cups]) if cups else 'empty'}")


# while choco and cups and milkshakes < 5:
#     curr_choco = choco.pop()
#     curr_cup = cups.popleft()
#     if curr_choco <= 0 and curr_cup <= 0:
#         continue
#     elif curr_choco <= 0:
#         cups.appendleft(curr_cup)
#         continue
#     elif curr_cup <= 0:
#         choco.append(curr_choco)
#         continue
#     elif curr_choco == curr_cup:
#         milkshakes += 1
#     else:
#         cups.append(curr_cup)
#         choco.append(curr_choco - 5)
#
# if milkshakes >= 5:
#     print(f'Great! You made all the chocolate milkshakes needed!')
# else:
#     print(f'Not enough milkshakes.')
# if choco:
#     # print(f"Chocolate: {', '.join([str(ch) for ch in choco])}")
#     print(f'Chocolate: ', end='')
#     print(*choco, sep=', ')
# else:
#     print('Chocolate: empty')
# if cups:
#     # print(f"Milk: {', '.join([str(cup) for cup in cups])}")
#     print(f'Milk: ', end='')
#     print(*cups, sep=', ')
# else:
#     print(f'Milk: empty')
