def selection_sort(sequence):
    for idx in range(len(sequence)):
        min_idx = idx
        for current_idx in range(idx + 1, len(sequence)):
            if sequence[current_idx] < sequence[min_idx]:
                min_idx = current_idx
        sequence[idx], sequence[min_idx] = sequence[min_idx], sequence[idx]
    return sequence


numbers = [int(x) for x in input().split()]
print(*selection_sort(numbers))
