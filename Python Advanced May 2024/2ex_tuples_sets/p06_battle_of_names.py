n = int(input())
odd = set()
even = set()

for index in range(1, n + 1):
    name = input()
    name_sum = 0    # name_sum = sum(ord(ch) for ch in input()) // index
    for char in name:
        name_sum += ord(char)
    name_sum //= index
    if name_sum % 2 != 0:
        odd.add(name_sum)
    else:
        even.add(name_sum)

odd_sum = sum(odd)
even_sum = sum(even)
if odd_sum == even_sum:
    print(*odd.union(even), sep=', ')
elif odd_sum > even_sum:
    print(*odd.difference(even), sep=', ')
elif even_sum > odd_sum:
    print(*odd.symmetric_difference(even), sep=', ')
