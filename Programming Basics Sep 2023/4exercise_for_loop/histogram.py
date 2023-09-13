n = int(input())
range1 = 0
range2 = 0
range3 = 0
range4 = 0
range5 = 0

for _ in range(n):
    current_number = int(input())
    if current_number < 200:
        range1 += 1
    elif 200 <= current_number <= 399:
        range2 += 1
    elif 400 <= current_number <= 599:
        range3 += 1
    elif 600 <= current_number <= 799:
        range4 += 1
    elif current_number >= 800:
        range5 += 1

p1 = range1 / n * 100
p2 = range2 / n * 100
p3 = range3 / n * 100
p4 = range4 / n * 100
p5 = range5 / n * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')