floors = int(input())
rooms = int(input())

room_number = 0
room_name = ''

for floor in range(floors, 0, -1):
    for room in range(rooms):

        if floor == floors:
            room_name = f'L{floor}{room}'
        elif floor % 2 == 0:
            room_name = f'O{floor}{room}'
        else:
            room_name = f'A{floor}{room}'

        print(room_name, end=' ')
    print('')

# method 2
# floors = int(input())
# rooms = int(input())
#
# for floor in range(floors, 0, -1):
#     for room in range(rooms):
#         if floor == floors:
#             print(f'L{floor}{room}', end=' ')
#         elif floor % 2 == 0:
#             print(f'O{floor}{room}', end=' ')
#         else:
#             print(f'A{floor}{room}', end=' ')
#     print('')