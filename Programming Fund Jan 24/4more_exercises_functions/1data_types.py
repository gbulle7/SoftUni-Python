def data_type(name, parameter):
    if name == 'int':
        return int(parameter) * 2
    elif name == 'real':
        result = float(parameter) * 1.5
        return f'{result:.2f}'
    else:
        return f'${parameter}$'


type = input()
value = input()
print(data_type(type, value))
