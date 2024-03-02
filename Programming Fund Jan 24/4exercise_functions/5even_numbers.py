sequence = list(map(int, input().split()))
# sequence = [int(integer) for integer in input().split()]


def even_numbers(number):
    return number % 2 == 0


print(list(filter(even_numbers, sequence)))

# One liner
# print(list(filter(lambda x: x % 2 == 0, map(int, input().split()))))
