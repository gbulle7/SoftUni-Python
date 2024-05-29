from collections import deque


def math_operations(*args, **kwargs):
    args = deque(args)

    def add(x):
        kwargs['a'] += x

    def subtract(x):
        kwargs['s'] -= x

    def divide(x):
        if x != 0:
            kwargs['d'] /= x

    def multiply(x):
        kwargs['m'] *= x

    mapper = {
        1: add,
        2: subtract,
        3: divide,
        4: multiply
    }

    while args:
        for i in range(1, 5):
            mapper[i](args.popleft())
            if not args:
                break

    result = ''
    sorted_data = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sorted_data:
        result += f"{key}: {value:.1f}\n"

    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))


# Method 2
# def math_operations(*args, **kwargs):
#     steps = 0
#     for num in args:
#         steps += 1
#         if steps == 1:
#             kwargs['a'] += num
#         elif steps == 2:
#             kwargs['s'] -= num
#         elif steps == 3:
#             if num != 0:
#                 kwargs['d'] /= num
#         elif steps == 4:
#             kwargs['m'] *= num
#             steps = 0
#
#     sorted_data = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))
#     # result = ''
#     # for key, value in sorted_data:
#     #     result += f'{key}: {value:.1f}\n'
#     # return result
#     return ''.join([f'{key}: {value:.1f}\n' for key, value in sorted_data])


# Method 3
# def math_operations(*args, **kwargs):
#     args = deque(args)
#     def func_a(k, v):
#         kwargs[k] += v
#     def func_s(k, v):
#         kwargs[k] -= v
#     def func_d(k, v):
#         if v != 0:
#             kwargs[k] /= v
#     def func_m(k, v):
#         kwargs[k] *= v
#
#     mapper = {1: lambda x: func_a('a', x),
#               2: lambda x: func_s('s', x),
#               3: lambda x: func_d('d', x),
#               4: lambda x: func_m('m', x)}
#
#     while args:
#         for i in range(1, 5):
#             mapper[i](args.popleft())
#             if not args:
#                 break
#
#     result = ''
#     sorted_data = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
#     for key, value in sorted_data:
#         result += f"{key}: {value:.1f}" + "\n"
#
#     return result


# Method 4
def math_operations(*args, **kwargs):
    for i in range(len(args)):
        if i % 4 == 0:
            kwargs['a'] += args[i]
        elif i % 4 == 1:
            kwargs['s'] -= args[i]
        elif i % 4 == 2:
            if not args[i] == 0:
                kwargs['d'] /= args[i]
        else:
            kwargs['m'] *= args[i]

    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join(f'{key}: {value:.1f}' for key, value in result)


# Method 5
def math_operations(*args, **kwargs):
    operations = {
        'a': lambda x, y: x + y,
        's': lambda x, y: x - y,
        'd': lambda x, y: x / y if y != 0 else x,
        'm': lambda x, y: x * y
    }
    keys = list(operations.keys())
    for i in range(len(args)):
        key = keys[i % 4]
        operation = operations[key]
        kwargs[key] = operation(kwargs[key], args[i])

    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join(f'{key}: {value:.1f}' for key, value in result)
