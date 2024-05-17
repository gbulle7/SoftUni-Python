from collections import deque

def robots_data_input():
    robots = input().split(";")
    robots_data = []
    for robot in robots:
        current_robot = robot.split("-")
        robot_name = current_robot[0]
        robot_process_time = int(current_robot[1])
        robot_available_time = robot_process_time
        robot_data = [robot_name, robot_process_time, robot_available_time, "free"]
        robots_data.append(robot_data)
    return robots_data              # list of robots


def start_time():
    hours, minutes, seconds = list(map(int, input().split(":")))
    time_in_seconds = hours * 3600 + minutes * 60 + seconds
    return time_in_seconds


def format_time(time_s):
    h = time_s // 3600 % 24
    m = time_s % 3600 // 60
    s = time_s % 3600 % 60
    return f'{h:02d}:{m:02d}:{s:02d}'


def product_complete(robot, product, time):
    time = format_time(time)
    print(f"{robot} - {product} [{time}]")


def main():
    robots_list = robots_data_input()
    global_time = start_time()
    product_queue = deque()

    product_name = input()
    while product_name != "End":
        product_queue.append(product_name)
        product_name = input()

    while product_queue:
        global_time += 1
        current_prod = product_queue.popleft()
        for robot in robots_list:
            name = robot[0]
            processing_time = robot[1]
            if robot[3] == "busy":
                robot[2] -= 1
                if robot[2] <= 0:
                    robot[2] = processing_time
                    robot[3] = "free"
            if robot[3] == "free":
                product_complete(name, current_prod, global_time)
                robot[3] = "busy"
                break
        else:
            product_queue.append(current_prod)


if __name__ == "__main__":
    main()


# from collections import deque
#
#
# def time_to_seconds(time):
#     hours, minutes, seconds = list(map(int, time.split(":")))
#     return hours * 60 * 60 + minutes * 60 + seconds
#
#
# def formatted_time(seconds):
#     hours = seconds // (60 * 60) % 24
#     minutes = (seconds % (60 * 60)) // 60
#     seconds = (seconds % (60 * 60)) % 60
#     return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#
#
# robots_info = input().split(";")
# robots = []
#
# for item in robots_info:
#     name, process_time = item.split("-")
#     robots.append([name, int(process_time), int(process_time), "free"])
#
# time = input()
# time_in_seconds = time_to_seconds(time)
# products_queue = deque()
# while True:
#     product = input()
#     if product == "End":
#         break
#     products_queue.append(product)
#
# while products_queue:
#     time_in_seconds += 1
#     current_product = products_queue.popleft()
#     for robot in robots:
#         robot_name = robot[0]
#         status = robot[3]
#         if status == "free":
#             robot[3] = "busy"
#             print(f"{robot_name} - {current_product} [{formatted_time(time_in_seconds)}]")
#             break
#     else:
#         products_queue.append(current_product)
#     for robot in robots:
#         if robot[3] == "busy":
#             robot[2] -= 1
#         if robot[2] <= 0:
#             robot[3] = "free"
#             robot[2] = robot[1]