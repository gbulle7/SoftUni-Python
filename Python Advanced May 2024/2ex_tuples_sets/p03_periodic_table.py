# print(*{element for _ in range(int(input())) for element in input().split()}, sep='\n')

n = int(input())
elements = set()

for _ in range(n):
    current_set = set(input().split())
    # elements = elements.union(current_set)
    # elements.update(current_set)
    elements |= current_set

print(*elements, sep='\n')
