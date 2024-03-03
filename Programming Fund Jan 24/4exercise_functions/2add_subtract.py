def sum_numbers(num1, num2):
    return num1 + num2


def subtract(result, num3):
    return result - num3


def add_and_subtract(num1, num2, num3):
    result = sum_numbers(num1, num2)
    return subtract(result, num3)


number1, number2, number3 = int(input()), int(input()), int(input())
print(add_and_subtract(number1, number2, number3))


# With Lambda functions
# sum_numbers = lambda num1, num2: num1 + num2
# subtract = lambda addition, num3: addition - num3
# sum_and_subtract = lambda num1, num2, num3: subtract(sum_numbers(num1, num2), num3)
# num1, num2, num3 = int(input()), int(input()), int(input())
# print(sum_and_subtract(num1, num2, num3))
