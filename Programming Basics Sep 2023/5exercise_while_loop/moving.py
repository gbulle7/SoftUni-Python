# method 1
width = int(input())
length = int(input())
height = int(input())
empty_space = width * length * height

while empty_space > 0:
    command = input()
    if command == 'Done':
        break
    boxes = int(command)
    empty_space -= boxes
difference = abs(empty_space)
if empty_space > 0:
    print(f'{difference} Cubic meters left.')
else:
    print(f'No more free space! You need {difference} Cubic meters more.')

# method 2
# width = int(input())
# length = int(input())
# height = int(input())
# empty_space = width * length * height
# have_space = True
# command = input()
#
# while command != 'Done':
#     boxes = int(command)
#     empty_space -= boxes
#     if empty_space <= 0:
#         have_space = False
#         break
#     command = input()
# if have_space:
#     print(f'{empty_space} Cubic meters left.')
# else:
#     print(f'No more free space! You need {abs(empty_space)} Cubic meters more.')