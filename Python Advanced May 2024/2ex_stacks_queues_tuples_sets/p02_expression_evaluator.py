from collections import deque

expression = input().split()
evaluator = deque()
result = 0

operations = {
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x // y
}

for char in expression:
    if char in operations:
        for num in range(len(evaluator) - 1):
            first_num = evaluator.popleft()
            second_num = evaluator.popleft()
            result = operations[char](first_num, second_num)
            evaluator.appendleft(result)
    else:
        evaluator.append(int(char))

print(result)