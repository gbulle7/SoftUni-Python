# optimised 6k+1, not working in Judge
# from math import isqrt
#
# def is_prime(n):
#     if n <= 3:
#         return n > 1
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     limit = isqrt(n)
#     for i in range(5, limit+1, 6):
#         if n % i == 0 or n % (i+2) == 0:
#             return False
#     return True
#
# number = int(input())
# print(is_prime(number))

number = int(input())
is_prime = True

for num in range(2, number):
    if number % num == 0:
        is_prime = False
print(is_prime)
