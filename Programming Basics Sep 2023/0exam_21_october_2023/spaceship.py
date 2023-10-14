width = float(input())
length = float(input())
height = float(input())
average_astronaut_height = float(input())

needed_room_height = average_astronaut_height + 0.4
room_volume = 2 * 2 * needed_room_height
spaceship_volume = width * length * height
astronauts_number = int(spaceship_volume / room_volume)

if astronauts_number < 3:
    print(f'The spacecraft is too small.')
elif astronauts_number <= 10:
    print(f'The spacecraft holds {astronauts_number} astronauts.')
else:
    print(f'The spacecraft is too big.')
