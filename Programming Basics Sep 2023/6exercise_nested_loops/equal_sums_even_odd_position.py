number1 = int(input())
number2 = int(input())

for number in range(number1, number2 + 1):
    string_number = str(number)
    sum_even = 0
    sum_odd = 0
    for index, digit in enumerate(string_number, 1):    # to start from index 1 - first index of the number, corresponding to the first digit is odd, the second is even..etc.
        if index % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)
    if sum_even == sum_odd:
        print(number, end=' ')
