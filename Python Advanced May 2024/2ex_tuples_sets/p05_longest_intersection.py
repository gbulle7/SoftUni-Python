# n = int(input())
# first_set = set()
# second_set = set()
# longest_intersection = set()
#
# for _ in range(n):
#     first, second = input().split('-')
#     first_start, first_end = first.split(',')
#     second_start, second_end = second.split(',')
#     for f_num in range(int(first_start), int(first_end) + 1):
#         first_set.add(f_num)
#     for s_num in range(int(second_start), int(second_end) + 1):
#         second_set.add(s_num)
#     current_intersection = first_set.intersection(second_set)
#     if len(current_intersection) > len(longest_intersection):
#         longest_intersection = current_intersection
#     first_set.clear()
#     second_set.clear()
#
# print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')

longest_intersection = set()
for _ in range(int(input())):
    first, second = input().split('-')
    first_start, first_end = first.split(',')       # first_start, first_end = map(int, first.split(','))
    second_start, second_end = second.split(',')    # second_start, second_end = map(int, second.split(','))
    first_set = set(range(int(first_start), int(first_end) + 1))
    second_set = set(range(int(second_start), int(second_end) + 1))
    intersection = first_set.intersection(second_set)
    # intersection = first_set & second_set
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')
