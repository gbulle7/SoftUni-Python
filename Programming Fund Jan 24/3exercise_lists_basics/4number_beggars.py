money = input().split(', ')
beggars = int(input())
money_list = []
for value in money:
    money_list.append(int(value))
# money_list = [int(value) for value in input().split(', ')]

money_saved = []
start_index = 0

for beggar in range(beggars):
    beggar_sum = 0
    for index in range(start_index, len(money_list), beggars):
        beggar_sum += money_list[index]
    money_saved.append(beggar_sum)
    start_index += 1

print(money_saved)

# money = [int(value) for value in input().split(', ')]
# beggars = int(input())
# money_earned = [0] * beggars
#
# for index, value in enumerate(money):
#     money_earned[index % beggars] += value
#
# print(money_earned)




