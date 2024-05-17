from collections import deque

# pumps = int(input())
# pumps_petrol_quantity = deque()
# distances_next_pumps = deque()
# own_petrol = 0
# trip_complete = False
# current_pump = 0
#
# for _ in range(pumps):
#     data = input().split()
#     petrol_quantity, distance_next = int(data[0]), int(data[1])
#     pumps_petrol_quantity.append(petrol_quantity)
#     distances_next_pumps.append(distance_next)
#
# while not trip_complete:
#     for curr_pump in range(len(pumps_petrol_quantity)):
#         petrol = pumps_petrol_quantity[curr_pump]
#         distance = distances_next_pumps[curr_pump]
#         own_petrol += petrol
#         own_petrol -= distance
#         if curr_pump == len(pumps_petrol_quantity) - 1:
#             if own_petrol >= 0:
#                 trip_complete = True
#                 break
#         if own_petrol < 0:
#             own_petrol = 0
#             pumps_petrol_quantity.append(pumps_petrol_quantity.popleft())
#             distances_next_pumps.append(distances_next_pumps.popleft())
#             break
#     if not trip_complete:
#         current_pump += 1
#
# print(current_pump)

pumps_num = int(input())
pumps = deque()
for _ in range(pumps_num):
    curr_fuel, curr_distance = input().split()
    pumps.append([int(curr_fuel), int(curr_distance)])
start_position = 0
stops = 0
while stops < pumps_num:
    fuel = 0
    for i in range(pumps_num):
        fuel += pumps[i][0]
        distance = pumps[i][1]
        if fuel < distance:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= distance
        stops += 1
print(start_position)