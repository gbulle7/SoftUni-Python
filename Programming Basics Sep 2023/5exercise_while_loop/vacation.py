needed_money = float(input())
current_balance = float(input())
days_saving = 0
spending_sequence = 0
not_saved = False

while current_balance < needed_money:
    operation = input()
    money = float(input())
    days_saving += 1
    if operation == 'save':
        current_balance += money
        spending_sequence = 0
    elif operation == 'spend':
        current_balance -= money
        if current_balance < 0:
            current_balance = 0
        spending_sequence += 1
        if spending_sequence >= 5:
            not_saved = True
            break
if not_saved:
    print('You can\'t save the money.')
    print(days_saving)
else:
    print(f'You saved the money for {days_saving} days.')