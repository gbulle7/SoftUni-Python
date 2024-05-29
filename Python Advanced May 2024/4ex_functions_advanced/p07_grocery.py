def grocery_store(**kwargs):
    store_sorted = sorted(kwargs.items(),
                          key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = ''   # result = []
    for name, quantity in store_sorted:
        result += f'{name}: {quantity}\n'    # result.append(f'{name}: {quantity}')
    return result                      # return '\n'.join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))


# Method 2
# def grocery_store(**kwargs):
#     store_sorted = sorted(kwargs.items(),
#                           key=lambda x: (-x[1], -len(x[0]), x[0]))
#
#     result = [f'{name}: {quantity}' for name, quantity in store_sorted]
#     return '\n'.join(result)
