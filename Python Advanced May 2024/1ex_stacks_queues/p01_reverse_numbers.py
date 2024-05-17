integers = input().split()
stack = []

for _ in range(len(integers)):
    stack.append(integers.pop())

print(" ".join(stack))