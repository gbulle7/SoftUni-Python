def recursive_power(number, power):
    result = 1
    if power == 0:
        return result
    result = number * recursive_power(number, power - 1)
    return result


print(recursive_power(2, 10))

# works in Judge
# def recursive_power(x, y):
#     return x ** y
