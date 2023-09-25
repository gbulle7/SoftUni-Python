# method 1
bottles_detergent = int(input())
detergent_quantity = bottles_detergent * 750
detergent_used = 0
washing_sequence = 0
clean_dishes = 0
clean_pots = 0

while detergent_quantity >= detergent_used:
    washing_sequence += 1
    command = input()
    if command == 'End':
        break
    crockery = int(command)
    if washing_sequence == 3:
        pots = crockery * 15
        clean_pots += crockery
        detergent_used += pots
        washing_sequence = 0
    else:
        dishes = crockery * 5
        clean_dishes += crockery
        detergent_used += dishes
difference = abs(detergent_quantity - detergent_used)
if detergent_quantity < detergent_used:
    print(f'Not enough detergent, {difference} ml. more necessary!')
else:
    print('Detergent was enough!')
    print(f'{clean_dishes} dishes and {clean_pots} pots were washed.')
    print(f'Leftover detergent {difference} ml.')

# method 2
# bottles_detergent = int(input())
# detergent_quantity = bottles_detergent * 750
# detergent_used = 0
# washing_sequence = 0
# clean_dishes = 0
# clean_pots = 0
# command = input()
#
# while command != 'End':
#     crockery = int(command)
#     washing_sequence += 1
#     if washing_sequence == 3:
#         pots = crockery * 15
#         clean_pots += crockery
#         detergent_used += pots
#         washing_sequence = 0
#     else:
#         dishes = crockery * 5
#         clean_dishes += crockery
#         detergent_used += dishes
#     if detergent_quantity < detergent_used:
#         break
#     command = input()
# difference = abs(detergent_quantity - detergent_used)
# if detergent_quantity < detergent_used:
#     print(f'Not enough detergent, {difference} ml. more necessary!')
# else:
#     print('Detergent was enough!')
#     print(f'{clean_dishes} dishes and {clean_pots} pots were washed.')
#     print(f'Leftover detergent {difference} ml.')
