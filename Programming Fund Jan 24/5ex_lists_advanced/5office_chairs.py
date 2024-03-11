rooms = int(input())
free_chairs = 0
enough_chairs = True

for room in range(1, rooms + 1):
    data = input().split()
    chairs = len(data[0])
    people = int(data[1])
    difference = abs(chairs - people)
    if chairs >= people:
        free_chairs += difference
    else:
        print(f'{difference} more chairs needed in room {room}')
        enough_chairs = False

if enough_chairs:
    print(f'Game On, {free_chairs} free chairs left')
