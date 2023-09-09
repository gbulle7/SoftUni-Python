def calculate_commission(city, sales_volume):
    commission_rates = {
        'Sofia': {500: 0.05, 1000: 0.07, 10000: 0.08, float('inf'): 0.12},
        'Varna': {500: 0.045, 1000: 0.075, 10000: 0.1, float('inf'): 0.13},
        'Plovdiv': {500: 0.055, 1000: 0.08, 10000: 0.12, float('inf'): 0.145}
    }

    if city not in commission_rates:
        return None, True

    for limit, rate in commission_rates[city].items():
        if sales_volume <= limit:
            return sales_volume * rate, False

def main():
    city = input('Enter the city: ')
    sales_volume = float(input('Enter the sales volume: '))

    fee, error_data = calculate_commission(city, sales_volume)

    if not error_data:
        print(f'Commission fee: {fee:.2f}')
    else:
        print('Error: Invalid city or sales volume.')

if __name__ == '__main__':
    main()