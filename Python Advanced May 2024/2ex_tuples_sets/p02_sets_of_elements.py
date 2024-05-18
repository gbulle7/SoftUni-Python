n, m = input().split()
first_set = set()
second_set = set()

for _ in range(int(n)):
    first_set.add(int(input()))

for _ in range(int(m)):
    second_set.add(int(input()))

print(*first_set.intersection(second_set), sep='\n')


# n, m = map(int, input().split())
# n_set = {input() for _ in range(n)}
# m_set = {input() for _ in range(m)}
# print(*n_set & m_set, sep='\n')
