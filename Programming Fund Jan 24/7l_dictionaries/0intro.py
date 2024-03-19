# Creating a dictionary
my_dict = {'fruit': 'apple', 'vegetable': 'cucumber'}
my_dict2 = dict(name="George", age=22)

# Iterating through key-value pairs
my_dict3 = {'fruit': 'apple',
            'vegetable': 'cucumber',
            'diary': 'milk'}
for key, value in my_dict3.items():
    print(f"Key: {key}; Value: {value}")

# Accessing values
my_dict4 = {'name':'Jack', 'age': 26}
print(my_dict4['name'])                 # Jack
print(my_dict4.get('age'))              # 26
# my_dict4['address']                    # KeyError
my_dict4.get('address')                 # None

# Updating/adding value
my_dict4['age'] = 27                    # update
print(my_dict4['age'])                  # 27
my_dict4['country'] = 'BG'              # add
print(my_dict4)                         # {'name': 'Jack', 'age': 27, 'country': 'BG'}

# Getting keys
my_dict5 = {1: 1, 2: 4, 3: 9}
for key in my_dict5.keys():
    print(key, end=" ") # 1 2 3

# Changing values by iterating through keys
my_dict6 = {1: 1, 2: 4, 3: 9}
for key in my_dict6.keys():              # = for key in squares
    my_dict6[key] *= 2
print(my_dict6)                          # {1: 2, 2: 8, 3: 18}

# Getting values
my_dict7 = {1: 1, 2: 4, 3: 9}
for value in my_dict7.values():          # for key in my_dict7.keys():
    print(value, end=" ")                # print(my_dict7[key], end=" ")


# Dictionary Methods
# Remove all the elements
my_dict8 = {1: 'apple', 2: 'banana'}
my_dict8.clear()
print(my_dict8)                         # {}

# Copy a dictionary - Is different from declaring a new variable with the same dictionary, because of "Mutable Aliasing"
# Appending to a list is changing(mutating) the list to both variables, unlike rebinding
my_dict9 = {1: 'apple', 2: 'banana'}
copied_dict = my_dict9.copy()
print(my_dict9 == copied_dict)           # True

# Removing a key-value and returning a value
my_dict10 = {"fruit": "apple", "vegetable": "cucumber"}
apple = my_dict10.pop("fruit")          # 'apple'
print(my_dict10)                        # {'vegetable': 'cucumber'}

# Removing and returning last key-value
my_dict11 = {"fruit": "apple", "vegetable": "cucumber"}
print(my_dict11.popitem())              # ("vegetable", "cucumber")
print(my_dict11)                        # {"fruit": "apple"}

# Deleting a key-value
my_dict12 = {"name": "George", "course": "Fundamentals"}
del my_dict12["course"]
print(my_dict12)                        # {"name": "George"}

# Deleting the dictionary completely
my_dict13 = {"name": "George", "course": "Fundamentals"}
del my_dict13
# print(my_dict13)                        # NameError


# Accessing an element from a nested dictionary
my_dict14 = {1: {'name': 'Peter', 'age': 22},
             2: {'name': 'Alex', 'age': 21}}
first_student_name = my_dict14[1]['name']
print(first_student_name)                # Peter


# Adding an element to a nested dictionary
my_dict14[3] = {}                       # {3: {}}
my_dict14[3]['name'] = 'Amy'            # {3: {'name': 'Amy'}}
my_dict14[3]['age'] = 25                # {3: {'name': 'Amy', 'age': 25}}


# Iterating through nested dictionary
shopping_list = {"foods": {"nuts": "almonds"},
                 "drinks": {"soft": "lemonade", "wine": "merlot"}
                 }
for key, value in shopping_list.items():
    for nested_key, nested_value in value.items():
        print(f'{nested_value} bought')
        shopping_list[key][nested_key] = 'bought'

# Creating a dictionary using dictionary comprehension
data = [("Peter", 22), ("Amy", 18), ("George", 35)]
dictionary = {key: value for (key, value) in data}    # {'Peter': 22, 'Amy': 18, 'George': 35}

nums = [1, 2, 3]
cubes = {num: num ** 3 for num in nums}               # {1: 1, 2: 8, 3: 27}

