def age_assignment(*args, **kwargs):
    [*names] = args
    persons_data = {}
    for name in names:
        persons_data[name] = 0
    for person in persons_data:
        for letter, age in kwargs.items():
            if letter in person:
                persons_data[person] = age

    persons_data = sorted(persons_data.items(), key=lambda x: x[0])   # sorted(persons_data.items())
    return ''.join([f'{p_name} is {p_age} years old.\n' for p_name, p_age in persons_data])


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


# Method 2
# def age_assignment(*args, **kwargs):
#     result = ""
#
#     for full_name in args:
#         first_letter = full_name[0]
#         kwargs[full_name] = kwargs[first_letter]
#         del kwargs[first_letter]
#
#     sorted_names = sorted(kwargs.items(), key=lambda x: x[0])
#
#     for name, age in sorted_names:
#         result += f"{name} is {age} years old." + "\n"
#
#     return result


# Method 3
# def age_assignment(*args, **kwargs):
#     persons = {name: kwargs[name[0]] for name in args}
#     persons = sorted(persons.items())
#     result = []
#     for name, age in persons:
#         result.append(f'{name} is {age} years old.')
#     return '\n'.join(result)
