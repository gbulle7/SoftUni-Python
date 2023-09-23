from math import pi

r = float(input())  # radius
area = pi * r ** 2  # r**2 = r*r
circumference = 2 * pi * r
print(f'{area:.2f}')
print(f'{circumference:.2f}')
