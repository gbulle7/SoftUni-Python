# rooms = int(input())
# free_chairs = 0
# enough_chairs = True
#
# for room in range(1, rooms + 1):
#     data = input().split()
#     chairs = len(data[0])
#     people = int(data[1])
#     difference = abs(chairs - people)
#     if chairs >= people:
#         free_chairs += difference
#     else:
#         print(f'{difference} more chairs needed in room {room}')
#         enough_chairs = False
#
# if enough_chairs:
#     print(f'Game On, {free_chairs} free chairs left')

def check_rooms(rms):
    free_chairs = 0
    for rms in range(1, rms + 1):
        current_chairs, people = input().split()
        difference = len(current_chairs) - int(people)
        if difference < 0:
            print(f'{abs(difference)} more chairs needed in room {rms}')
        free_chairs += difference

    return free_chairs


rooms = int(input())
total_free_chairs = check_rooms(rooms)
if total_free_chairs >= 0:
    print(f'Game On, {total_free_chairs} free chairs left')
