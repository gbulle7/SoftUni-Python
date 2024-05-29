def concatenate(*args, **kwargs):
    result = ''
    for arg in args:
        result += arg
    for k, v in kwargs.items():
        result = result.replace(k, v)
    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))


# Method 2
# def concatenate(*args, **kwargs):
#     result = "".join(args)
#
#     for key in kwargs:
#         if key in result:
#             result = result.replace(key, kwargs[key])
#
#     return result
