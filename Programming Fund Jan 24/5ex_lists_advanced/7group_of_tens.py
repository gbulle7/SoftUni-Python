sequence = list(map(int, input().split(', ')))

for group in range(1, 11):
    if len(sequence) == 0:
        break

    group_list = [num for num in sequence if num <= (group * 10)]
    sequence = [num for num in sequence if num not in group_list]
    print(f"Group of {group}0's: {group_list}")
