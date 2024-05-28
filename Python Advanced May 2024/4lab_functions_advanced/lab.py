# Packing args into tuple
def some_func(*args):
    print(args)
some_func(1, 2, 3)               # (1, 2, 3)
some_func("simon", "george")     # ("simon", "george")
some_func(True, False)           # (True, False)
some_func()                            # ()


# Packing kwargs into dict
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print(f"{value}, {key}")
greet_me(Simon="Hello", George="Bye")
# Hello, Simon
# Bye, George


# Unpacking list
def print_nums(a, b, c):
    print(a, b, c)
nums = [1, 2, 3]
print_nums(*nums)        # 1 2 3


# Unpacking dict
def some_func(name, age):
    print(f"{name} is {age} years old")
person = {'age': 26, 'name': "Simon"}
some_func(**person)       # Simon is 26 years old


# Sort by value reversed, then by key
my_dict = {'Simon': 16, 'Test': 18, 'George': 18, 'John': 45}
sorted_dict = sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))
print(sorted_dict)
# [('John', 45), ('George', 18), ('Test', 18), ('Simon', 16)]


# Function returning function
def calculator(operator):
    def addition(a, b):
        return a + b
    def subtraction(a, b):
        return a - b
    if operator == "+":
        return addition
    elif operator == "-":
        return subtraction
operation = calculator("+")
result = operation(2, 3)
print(result)       # 5


# Closures
def outside_function(number):
    def inside_function():
        return number
    return inside_function
print(outside_function(10)())   # 10

def greeting(name):
    hello = "Hello, "
    def say_hi():
        return hello + name
    return say_hi
print(greeting("Peter")())       # Hello, Simon


# Recursion
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
