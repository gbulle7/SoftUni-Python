from collections import deque

green_light_duration = int(input())
free_windows_duration = int(input())
command = input()
queue = deque()
crash = False
passed_cars = 0

while command != "END" and not crash:
    if command == "green":
        green_time = green_light_duration
        car_inside = deque()
        while green_time and queue:
            green_time -= 1
            car_outside = queue[0]
            car_inside.append(car_outside.popleft())

            if not car_outside:
                queue.popleft()
                passed_cars += 1
                car_inside = deque()

        window = free_windows_duration
        while window and car_inside:
            window -= 1
            car_outside = queue[0]
            car_inside.append(car_outside.popleft())
            if not car_outside:
                queue.popleft()
                passed_cars += 1
                car_inside = deque()
        if car_inside:
            crash = True
            car = f"{(''.join(car_inside))}{(''.join(car_outside))}"
            break
    queue.append(deque(command))
    command = input()

if crash:
    print("A crash happened!")
    print(f"{car} was hit at {car_outside[0]}.")
else:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")


# from collections import deque
#
# green_light = int(input())
# free_window = int(input())
# time_to_enter = green_light
# passed_time = 0
#
# cars = deque()
# passed_cars = 0
# crash = False
#
# while True:
#     command = input()
#     if command == "END":
#         print("Everyone is safe.")
#         print(f"{passed_cars} total cars passed the crossroads.")
#         break
#     elif command == "green":
#         while cars:
#             if time_to_enter <= 0:
#                 break
#             current_car = cars.popleft()
#             car_size = len(current_car)
#             available_time = time_to_enter + free_window
#             if car_size <= available_time:
#                 passed_cars += 1
#                 time_to_enter -= len(current_car)
#             else:
#                 crash = True
#                 print("A crash happened!")
#                 print(f"{current_car} was hit at {current_car[available_time]}.")
#                 break
#         time_to_enter = green_light
#     else:
#         cars.append(command)
#     if crash:
#         break
