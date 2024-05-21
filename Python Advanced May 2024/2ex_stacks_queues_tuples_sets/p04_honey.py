from collections import deque

bees = deque(map(int, input().split()))
nectar_values = list(map(int, input().split()))
symbols = deque(input().split())
total_honey = 0

operations = {
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y if y != 0 else 0
}

while bees and nectar_values:
    bee = bees.popleft()
    nectar = nectar_values.pop()
    if nectar >= bee:
        symbol = symbols.popleft()
        total_honey += abs(operations[symbol](bee, nectar))
    else:
        bees.appendleft(bee)


# def calculate_honey(matched_bee, matched_nectar, operator):
#     if operator == '/' and matched_nectar == 0:
#         return 0
#     else:
#         return eval(f'{matched_bee}{operator}{matched_nectar}')
#
#
# while bees and nectar_values:
#     bee = bees.popleft()
#     nectar = nectar_values.pop()
#     if nectar >= bee:
#         symbol = symbols.popleft()
#         total_honey += abs(calculate_honey(bee, nectar, symbol))
#     else:
#         bees.appendleft(bee)

print(f'Total honey made: {total_honey}')
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar_values:
    print(f"Nectar left: {', '.join(map(str, nectar_values))}")
