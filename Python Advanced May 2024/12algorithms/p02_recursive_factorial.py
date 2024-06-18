def recursive_factorial(num):
    if num == 0:    # to cover 0! = 1 case
        return 1
    return num * recursive_factorial(num - 1)


number = int(input())
print(recursive_factorial(number))
