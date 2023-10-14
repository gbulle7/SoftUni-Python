locations_number = int(input())

for _ in range(locations_number):
    gold_per_location = 0
    expected_average_daily_gold = float(input())
    days_mined = int(input())
    for day in range(days_mined):
        daily_mined_gold = float(input())
        gold_per_location += daily_mined_gold
    actual_average_gold = f'{(gold_per_location / days_mined):.2f}'
    if expected_average_daily_gold <= float(actual_average_gold):
        print(f'Good job! Average gold per day: {actual_average_gold}.')
    else:
        needed_gold = expected_average_daily_gold - float(actual_average_gold)
        print(f'You need {needed_gold:.2f} gold.')
