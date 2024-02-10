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

# factorial with list
# a = int(input())
# lst = [a for _ in range(a)]

# factorial with numpy
# import numpy
# n=5
# x=numpy.prod([i for i in range(1,n+1)])
# print(x)