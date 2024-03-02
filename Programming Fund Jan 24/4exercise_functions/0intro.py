# DOCstring
# def add_numbers(x, y):
#     """This is Docstring. Adds numbers and return result."""
#     return x + y
# result = add_numbers(3, 5)
# print('Result:', result)
# print(add_numbers.__doc__)


# Declaring named parameters, specify int Type, annotation Str return
# def greet(name, age: int, message = 'Hello') -> str:
#     return f'{message}, {name}, {age}!'
# print(greet('Nombre', 21))
# print(greet(message = 'Hi there', name='Llama', age=18))


# Mapping with lambda function
# nums = [1, 2, 3, 4, 5, 6]
# doubled_nums = list(map(lambda x: x * 2, nums))
# print(doubled_nums)


# Recursive function
# def count_recursive(n):
#     if n == 1:
#         print(n)
#     else:
#         count_recursive(n - 1)
#         print(n)
# count_recursive(10)


# Multiple values in a function
# def calculate_stats(numbers):
#     total_sum = sum(numbers)
#     average_number = total_sum / len(numbers)
#     max_number = max(numbers)
#     min_number = min(numbers)
#     return total_sum, average_number, max_number, min_number
# data = [10, 50, 30, 20, 40]
# total, average, maximum, minimum = calculate_stats(data)
# print('Data:', data)
# print('Total:', total)
# print('Average:', average)
# print('Maximum:', maximum)
# print('Minimum:', minimum)


# After return of inner function continues back to outer
# def outer_function():
#     print("This is the outer function.")
#
#     def inner_function():
#         print("This is the inner function.")
#         return  # Inner function returns here
#
#     inner_function()  # Call the inner function
#     print("Back to the outer function.")
#
# outer_function()