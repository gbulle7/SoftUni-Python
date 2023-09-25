target_sum = int(input())
total_collected_money = 0
collected_cash = 0
transactions_cash = 0
collected_card = 0
transactions_card = 0
counter = 0
invalid_operation = False

while total_collected_money < target_sum:
    command = input()
    if command == 'End':
        print(f'Failed to collect required money for charity.')
        break
    current_money = int(command)
    if counter % 2 == 0:
        if current_money <= 100:
            collected_cash += current_money
            transactions_cash += 1
            total_collected_money += current_money
        else:
            invalid_operation = True
    else:
        if current_money >= 10:
            collected_card += current_money
            transactions_card += 1
            total_collected_money += current_money
        else:
            invalid_operation = True
    if invalid_operation:
        print('Error in transaction!')
    else:
        print('Product sold!')
    counter += 1
    invalid_operation = False
else:
    average_cash = collected_cash / transactions_cash
    average_card = collected_card / transactions_card
    print(f'Average CS: {average_cash:.2f}')
    print(f'Average CC: {average_card:.2f}')
