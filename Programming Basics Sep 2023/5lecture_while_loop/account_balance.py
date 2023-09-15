# with while True
total_sum = 0

while True:
    current_money = input()
    if current_money == 'NoMoreMoney':
        break
    elif float(current_money) < 0:
        print('Invalid operation!')
        break
    total_sum += float(current_money)
    print(f'Increase: {float(current_money):.2f}')
print(f'Total: {total_sum:.2f}')

# with while
# current_money = input()
# total_sum = 0
#
# while current_money != 'NoMoreMoney':
#     amount = float(current_money)
#     if amount < 0:
#         print('Invalid operation!')
#         break
#     total_sum += amount
#     print(f'Increase: {amount:.2f}')
#     current_money = input()
# print(f'Total: {total_sum:.2f}')