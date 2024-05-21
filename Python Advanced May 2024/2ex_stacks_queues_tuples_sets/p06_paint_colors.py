from collections import deque

line = deque(input().split())
main_colors = ['red', 'yellow', 'blue']
secondary_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['blue', 'red'],
    'green': ['yellow', 'blue']
}
colors_collected = []

while line:
    first = line.popleft()
    last = line.pop() if line else ''
    for color in (first + last, last + first):
        if color in main_colors or color in secondary_colors:
            colors_collected.append(color)
            break
    else:
        if len(last) > 1:
            line.insert(len(line) // 2, last[:-1])
        if len(first) > 1:
            line.insert(len(line) // 2, first[:-1])

for color in colors_collected:
    if color in secondary_colors:
        for element in secondary_colors[color]:
            if element not in colors_collected:
                colors_collected.remove(color)
                break

print(colors_collected)
