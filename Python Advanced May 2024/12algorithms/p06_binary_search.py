def binary_search(sequence, number):
    left_index = 0
    right_index = len(sequence) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if sequence[mid_index] == number:
            return mid_index

        if sequence[mid_index] < number:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1   # if number is not present, traditionally return -1


array = [int(x) for x in input().split()]
num = int(input())
print(binary_search(array, num))
