# Fibonacci Sequence
# def fibonacci_sequence(num):
#   if num == 0:
#     return [0]
#   fibonacci_list = [0, 1]
#   for _ in range(1, num):
#     next_number = fibonacci_list[-1] + fibonacci_list[-2]
#     fibonacci_list.append(next_number)
#   return fibonacci_list
# number = abs(int(input()))
# print(fibonacci_sequence(number))


# fibonacci with list
# x = int(input())
# lst = [0, 1]
#
# for _ in range(x - 1):
#     a = lst[0] + lst[1]
#     lst.append(a)
#     lst.pop(0)
# print(lst[1])

# fibonacci with function
# def fibonacci(x):
#     if x <= 1:
#         return x
#     else:
#         return fibonacci(x-1) + fibonacci(x-2)
# a = int(input())
# print(fibonacci(a))


# Factorial with Reduce method
# from functools import reduce
# number = int(input())
# numbers = []
# for _ in range(number):
#     numbers.append(number)
#     number -= 1
# result = reduce(lambda a, b: a * b, numbers)
# print(result)


# factorial with math lib
# from math import factorial
# print(factorial(5))

# factorial with for loop
# a = int(input())
# b = 1
# for _ in range(a):
#     b *= a
#     a -= 1
# print(b)

# factorial with function
# def factorial(x):
#     if x == 0:
#         return 1
#     else:
#         return x * factorial(x-1)
# a = int(input())
# print(factorial(a))


# factorial with numpy
# import numpy
# n=5
# x=numpy.prod([i for i in range(1,n+1)])
# print(x)
