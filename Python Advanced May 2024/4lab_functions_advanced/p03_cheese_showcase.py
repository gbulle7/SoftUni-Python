def sorting_cheeses(**cheeses_dict):
    cheeses_sorted = sorted(
        cheeses_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for name, quantity in cheeses_sorted:
        result.append(name)
        quantity_list = sorted(quantity, reverse=True)  # instead of reverse, key=lambda x: -x)
        result += quantity_list
    return '\n'.join(map(str, result))
    # return '\n'.join([str(x) for x in result])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
