divisor = int(input())
boundary = int(input())

for _ in range(boundary):
    if boundary > 0 and boundary % divisor == 0:
        break
    else:
        boundary -= 1
print(boundary)