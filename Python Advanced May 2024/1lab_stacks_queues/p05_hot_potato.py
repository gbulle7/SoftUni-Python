from collections import deque
names = input().split()
toss = int(input())
queue = deque(names)

while len(queue) > 1:
    for index in range(1, toss):
        queue.append(queue.popleft())
    print(f"Removed {queue.popleft()}")

print(f"Last is {queue.pop()}")


# kids = deque(input().split())
# n = int(input()) - 1
# while len(kids) > 1:
#     kids.rotate(-n)
#     print(f"Removed {kids.popleft()}")
# print(f"Last is {queue.pop()}")