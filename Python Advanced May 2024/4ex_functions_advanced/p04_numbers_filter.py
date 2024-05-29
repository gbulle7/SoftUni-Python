def even_odd_filter(**kwargs):
    numbers = dict()
    for k, v in kwargs.items():
        if k == 'odd':
            numbers[k] = list(filter(lambda kvp: kvp % 2 != 0, v))
        elif k == 'even':
            numbers[k] = list(filter(lambda kvp: kvp % 2 == 0, v))

    return {key: value for key, value in sorted(numbers.items(), key=lambda x: -len(x[1]))}


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))


# Method 2
def even_odd_filter(**kwargs):
    for k, v in kwargs.items():
        if k == 'even':
            kwargs[k] = [x for x in v if x % 2 == 0]
        else:
            kwargs[k] = [x for x in v if x % 2 != 0]

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


# Method 3
def even_odd_filter(**kwargs):
    kwargs = {key: [x for x in num if x % 2 == (0 if key == 'even' else 1)] for key, num in kwargs.items()}
    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


# Method 4
# def even_odd_filter(**kwargs):
#     result = {}
#
#     for key in kwargs:
#         if key == "odd":
#             result[key] = [x for x in kwargs[key] if x % 2 != 0]
#         else:
#             result[key] = [x for x in kwargs[key] if x % 2 == 0]
#
#     return dict(sorted(result.items(), key = lambda x: -len(x[1])))
