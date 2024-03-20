def binary_search(nums, target):
    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_element = nums[middle_index]

        if middle_element == target:
            return middle_index

        if middle_element < target:
            left_index = middle_index + 1
        elif target < middle_element:
            right_index = middle_index - 1


data = [int(number) for number in input().split()]
target_number = int(input('Target Number: '))

output = binary_search(data, target_number)
print(f'Data: {data}')
print(f'Target Index: {output}')
