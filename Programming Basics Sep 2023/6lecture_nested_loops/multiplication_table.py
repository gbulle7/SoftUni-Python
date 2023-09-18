for multiplicand in range(1, 11):
    for multiplier in range(1, 11):
        product = multiplicand * multiplier
        print(f'{multiplicand} * {multiplier} = {product}')

# method 2
# multiplicand = 0
# multiplier = 0
#
# for _ in range(10):
#     multiplicand += 1
#     multiplier = 0
#     for _ in range(10):
#         multiplier += 1
#         result = multiplicand * multiplier
#         print(f'{multiplicand} * {multiplier} = {result}')

# method 3
# for multiplicand in range(10):
#     multiplicand += 1
#     for multiplier in range(10):
#         multiplier += 1
#         result = multiplicand * multiplier
#         print(f'{multiplicand} * {multiplier} = {result}')

# method 4 While Loop
# multiplicand = 0
# multiplier = 0
#
# while multiplicand < 10:
#     multiplicand += 1
#     multiplier = 0
#     while multiplier < 10:
#         multiplier += 1
#         product = multiplicand * multiplier
#         print(f'{multiplicand} * {multiplier} = {product}')