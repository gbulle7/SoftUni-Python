stadium_capacity = int(input())
total_fans = int(input())
total_fans_a = 0
total_fans_b = 0
total_fans_v = 0
total_fans_g = 0

for _ in range(total_fans):
    current_sector = input()
    if current_sector == 'A':
        total_fans_a += 1
    elif current_sector == 'B':
        total_fans_b += 1
    elif current_sector == 'V':
        total_fans_v += 1
    else:
        total_fans_g += 1
percentage_a = total_fans_a / total_fans * 100
percentage_b = total_fans_b / total_fans * 100
percentage_v = total_fans_v / total_fans * 100
percentage_g = total_fans_g / total_fans * 100
total_fans_percentage = total_fans / stadium_capacity * 100
print(f'{percentage_a:.2f}%')
print(f'{percentage_b:.2f}%')
print(f'{percentage_v:.2f}%')
print(f'{percentage_g:.2f}%')
print(f'{total_fans_percentage:.2f}%')


