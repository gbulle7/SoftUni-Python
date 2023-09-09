record = float(input())
distance = float(input())
time_swimming_meter = float(input())
slowing = (distance // 15) * 12.5  # every 15 m of the distance, resistance slowing by 12.5 sec
time_swimming = time_swimming_meter * distance + slowing
if time_swimming < record:
    print(f'Yes, he succeeded! The new world record is {time_swimming:.2f} seconds.')
else:
    time_slower = record - time_swimming
    print(f'No, he failed! He was {time_slower:.2f} seconds slower.')
