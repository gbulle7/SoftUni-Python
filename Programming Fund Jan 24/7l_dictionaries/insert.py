# Existing dictionary
existing_dict = {'a': 1, 'b': 2, 'c': 3}

# New key-value pair to insert
new_key = 'x'
new_value = 10

# Inserting the new key-value pair between 'b' and 'c'
new_dict = {}
for key, value in existing_dict.items():
    new_dict[key] = value
    if key == 'b':
        new_dict[new_key] = new_value

print(new_dict)