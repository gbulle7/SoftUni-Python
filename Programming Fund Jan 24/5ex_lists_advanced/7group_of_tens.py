sequence = list(map(int, input().split(', ')))

for group in range(1, 11):
    if len(sequence) == 0:
        break

    group_list = [num for num in sequence if num <= (group * 10)]
    sequence = [num for num in sequence if num not in group_list]
    print(f"Group of {group}0's: {group_list}")


# numbers = [int(number) for number in input().split(", ")]
# current_group = 10
# while numbers:
#     filtered_numbers_for_current_group = [number for number in numbers if number <= current_group]
#     print(f"Group of {current_group}'s: {filtered_numbers_for_current_group}")
#     current_group += 10
#     numbers = [number for number in numbers if number not in filtered_numbers_for_current_group]
