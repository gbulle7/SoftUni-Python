from math import pi

figure = input()
if figure == "square":
    a = float(input())
    area_square = a * a
    print(f"{area_square:.3f}")
elif figure == "rectangle":
    b = float(input())
    c = float(input())
    area_rectangle = b * c
    print(f"{area_rectangle:.3f}")
elif figure == "circle":
    r = float(input())
    area_circle = pi * r**2
    print(f"{area_circle:.3f}")
elif figure == "triangle":
    d = float(input())
    h = float(input())
    area_triangle = d * h / 2
    print(f"{area_triangle:.3f}")
