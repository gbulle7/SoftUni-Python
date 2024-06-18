def bubble_sort(sequence):
    is_sorted = False
    s = 0

    while not is_sorted:
        is_sorted = True
        for i in range(1, len(sequence) - s):
            if sequence[i - 1] > sequence[i]:
                is_sorted = False
                sequence[i], sequence[i - 1] = sequence[i - 1], sequence[i]

        s += 1


numbers = [int(x) for x in input().split()]
bubble_sort(numbers)
print(*numbers)
