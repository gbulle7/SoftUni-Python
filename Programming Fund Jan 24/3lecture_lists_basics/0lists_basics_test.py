numbers = [2, 4, 6, 8, 10]
result = [i for i in numbers if all(i % j != 0 for j in range(2, i))]
print(result)   # 2

# [create a list consisting of each element for the same element in the list "numbers",
# if every cycle of the inside for-loop is True for the following equation:
# the same element % the index of the current cycle of the for loop in range (2, the same element)
