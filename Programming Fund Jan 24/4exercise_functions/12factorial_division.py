# def factorial_division(n1, n2):
#     factorial_one = 1
#     factorial_two = 1
#     for mul1 in range(1, n1 + 1):
#         factorial_one *= mul1
#     for mul2 in range(1, n2 + 1):
#         factorial_two *= mul2
#     return f'{(factorial_one / factorial_two):.2f}'
#
#
# num1 = int(input())
# num2 = int(input())
# print(factorial_division(num1, num2))


# def factorial_division(first: int, second: int):
#     for factorial in range(1, first):
#         first *= factorial
#     for factorial in range(1, second):
#         second *= factorial
#     division = first / second
#     return f'{division:.2f}'
#
#
# first_number = int(input())
# second_number = int(input())
# print(factorial_division(first_number, second_number))


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def factorial_division(num1, num2):
    result1 = factorial(num1)
    result2 = factorial(num2)
    return f'{(result1 / result2):.2f}'


number1 = int(input())
number2 = int(input())
print(factorial_division(number1, number2))
