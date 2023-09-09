city = input()
sales_volume = float(input())
commission = 0
error_data = False

if city == 'Sofia':
    if 0 <= sales_volume <= 500:
        commission = 0.05
    elif 500 < sales_volume <= 1000:
        commission = 0.07
    elif 1000 < sales_volume <= 10000:
        commission = 0.08
    elif sales_volume > 10000:
        commission = 0.12
    else:
        error_data = True

elif city == 'Varna':
    if 0 <= sales_volume <= 500:
        commission = 0.045
    elif 500 < sales_volume <= 1000:
        commission = 0.075
    elif 1000 < sales_volume <= 10000:
        commission = 0.1
    elif sales_volume > 10000:
        commission = 0.13
    else:
        error_data = True

elif city == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        commission = 0.055
    elif 500 < sales_volume <= 1000:
        commission = 0.08
    elif 1000 < sales_volume <= 10000:
        commission = 0.12
    elif sales_volume > 10000:
        commission = 0.145
    else:
        error_data = True

else:
    error_data = True

if not error_data:
    fee = sales_volume * commission
    print(f'{fee:.2f}')
else:
    print('error')
