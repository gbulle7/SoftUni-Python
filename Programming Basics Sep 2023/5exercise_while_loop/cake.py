# method 1
width = int(input())
length = int(input())
size = width * length

while size > 0:
    command = input()
    if command == 'STOP':
        break
    pieces = int(command)
    size -= pieces
if size < 0:
    print(f'No more cake left! You need {abs(size)} pieces more.')
else:
    print(f'{size} pieces are left.')

# method 2
# width = int(input())
# length = int(input())
# size = width * length
# is_empty = False
# command = input()
#
# while command != 'STOP':
#     pieces = int(command)
#     size -= pieces
#     if size <= 0:
#         is_empty = True
#         break
#     command = input()
# if is_empty:
#     print(f'No more cake left! You need {abs(size)} pieces more.')
# else:
#     print(f'{size} pieces are left.')
