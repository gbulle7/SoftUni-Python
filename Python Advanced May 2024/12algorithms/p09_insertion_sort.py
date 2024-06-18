def insertion_sort(sequence):
    for j in range(1, len(sequence)):
        key = sequence[j]
        i = j - 1

        while i >= 0 and key < sequence[i]:
            sequence[i + 1] = sequence[i]
            i -= 1

        sequence[i + 1] = key
    return sequence


numbers = [int(x) for x in input().split()]
sorted_nums = insertion_sort(numbers)
print(*sorted_nums)
