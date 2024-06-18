def array_sum(array, index):
    if index == len(array) - 1:
        return array[index]
    return array[index] + array_sum(array, index + 1)


numbers = list(map(int, input().split()))
# numbers = [int(x) for x in input().split()]

print(array_sum(numbers, 0))
