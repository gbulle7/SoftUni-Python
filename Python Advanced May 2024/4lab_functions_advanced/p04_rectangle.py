def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return f'Enter valid values!'

    def area(a, b):     # def area()
        return a * b    # return length * width

    def perimeter(a, b):       # def perimeter()
        return (a + b) * 2     # return (length + width) * 2

    return f'Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}'


print(rectangle(2, 10))
