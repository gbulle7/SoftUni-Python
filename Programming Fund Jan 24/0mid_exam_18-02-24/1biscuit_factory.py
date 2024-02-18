biscuits_worker_day = int(input())
count_workers = int(input())
compet_biscuits_month = int(input())

biscuits_month = 0

for day in range(1, 30 + 1):
    biscuits_day = count_workers * biscuits_worker_day
    if day % 3 == 0:
        biscuits_day *= 0.75
    biscuits_month += int(biscuits_day)

print(f'You have produced {biscuits_month} biscuits for the past month.')

if biscuits_month > compet_biscuits_month:
    perc_diff = biscuits_month / compet_biscuits_month * 100 - 100
    print(f'You produce {perc_diff:.2f} percent more biscuits.')
else:
    perc_diff = (compet_biscuits_month - biscuits_month) / compet_biscuits_month * 100
    print(f'You produce {perc_diff:.2f} percent less biscuits.')



