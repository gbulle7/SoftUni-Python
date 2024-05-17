integers = [int(x) for x in input().split()]
rack_capacity = int(input())
# current_rack = rack_capacity
# racks = 1
#
# while len(integers) > 0:
#     if current_rack - integers[-1] >= 0:
#         current_rack -= integers.pop()
#     else:
#         racks += 1
#         current_rack = rack_capacity
# print(racks)

racks = 0
while integers:
    racks += 1
    current_rack = rack_capacity
    while integers and integers[-1] <= current_rack:
        current_rack -= integers.pop()
print(racks)
