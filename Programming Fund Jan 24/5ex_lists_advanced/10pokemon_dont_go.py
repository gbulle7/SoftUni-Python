sequence = list(map(int, input().split()))
elements_sum = 0

while len(sequence) > 0:
    index = int(input())
    if 0 <= index < len(sequence):
        current_element = sequence.pop(index)
    elif index < 0:
        current_element = sequence[0]
        sequence[0] = sequence[-1]
    else:
        current_element = sequence[-1]
        sequence[-1] = sequence[0]

    elements_sum += current_element

    for indx, element in enumerate(sequence):
        if element <= current_element:
            sequence[indx] += current_element
        else:
            sequence[indx] -= current_element

print(elements_sum)
