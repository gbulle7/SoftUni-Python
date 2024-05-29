def even_odd(*args):
    if args[-1] == 'even':
        return [x for x in args[:-1] if x % 2 == 0]
    # return [x for x in args[:-1] if x % 2 != 0]
    elif args[-1] == 'odd':
        return [x for x in args[:-1] if x % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

# Method 2
# def even_odd(*args):
#     *numbers, command = args
#     result = []
#
#     if command == "even":
#         [result.append(x) for x in numbers if x % 2 == 0]
#     elif command == "odd":
#         [result.append(x) for x in numbers if x % 2 != 0]
#
#     return result
