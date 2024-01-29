def calculate_price(product, quantity):
    value = None
    if product == 'coffee':
        value = 1.5
    elif product == 'water':
        value = 1
    elif product == 'coke':
        value = 1.4
    elif product == 'snacks':
        value = 2
    return quantity * value


item = input()
number = int(input())
total_price = calculate_price(item, number)
print(f'{total_price:.2f}')

#  check Lecturer's solution, more simple