mapper = {
    '/': lambda x, y: x / y if y != 0 else 'Division by Zero',
    '*': lambda x, y: x * y,
    '-': lambda x, y: x - y,
    '+': lambda x, y: x + y,
    '^': lambda x, y: x ** y
}


def math_operations(num1, sign, num2):
    result = mapper[sign](float(num1), float(num2))
    return f'{result:.2f}' if isinstance(result, float) else result
