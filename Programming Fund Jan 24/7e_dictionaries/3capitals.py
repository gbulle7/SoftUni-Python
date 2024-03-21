country = input().split(', ')
city = input().split(', ')

capital_dict = dict(zip(country, city))

# capital_dict = dict(map(lambda i, j: (i, j), country, city))

# capital_dict = {country[index]:city[index] for index in range(len(country))}

for k, v in capital_dict.items():
    print(f'{k} -> {v}')
