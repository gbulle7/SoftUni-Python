operator = input()
first_num = int(input())
second_num = int(input())

def calculate(a, b):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = int(a / b)  # wrong in SoftUni, for example 5/3 is 1.66 but this returns 1
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    return result


print(calculate(first_num, second_num))


