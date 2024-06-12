def cookbook(*cuisines):
    cuisines_dict = {}
    for cuisine in cuisines:
        if cuisine[1] not in cuisines_dict:
            cuisines_dict[cuisine[1]] = {}
        cuisines_dict[cuisine[1]].update({cuisine[0]: cuisine[2]})

    sorted_cuisines = sorted(cuisines_dict.items(), key=lambda kvp: (-(len(kvp[1])), kvp[0]))

    result = ''
    for cuisine, recipes in sorted_cuisines:
        sorted_recipes = sorted(recipes.items(), key=lambda kvp: kvp[0])
        result += f'{cuisine} cuisine contains {len(sorted_recipes)} recipes:\n'
        for recipe, ingredients in sorted_recipes:
            result += f"  * {recipe} -> Ingredients: {', '.join(ingredients)}\n"
    return result


# Data

# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))

# print(cookbook(
#     ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
#     ))

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))

# Method 2
# def cookbook(*cuisines):
#     cuisines_dict = {}
#     for cuisine in cuisines:
#         if cuisine[1] not in cuisines_dict:
#             cuisines_dict[cuisine[1]] = {}
#         cuisines_dict[cuisine[1]].update({cuisine[0]: cuisine[2]})
#
#     for cuisine, recipes in cuisines_dict.items():
#         sorted_recipes = sorted(recipes.items(), key=lambda kvp: kvp[0])
#         cuisines_dict[cuisine] = sorted_recipes
#
#     sorted_cuisines = sorted(cuisines_dict.items(), key=lambda kvp: (-(len(kvp[1])), kvp[0]))
#
#     result = ''
#     for cuisine, recipes in sorted_cuisines:
#         result += f'{cuisine} cuisine contains {len(recipes)} recipes:\n'
#         for recipe, ingredients in recipes:
#             result += f"  * {recipe} -> Ingredients: {', '.join(ingredients)}\n"
#     return result
