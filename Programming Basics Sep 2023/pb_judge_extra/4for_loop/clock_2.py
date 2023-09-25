# with For Loop
for hours in range(0, 24):
    for minutes in range(0, 60):
        for seconds in range(0, 60):
            print(f'{hours} : {minutes} : {seconds}')

# with While Loop
# seconds = 0
# minutes = 0
# hours = 0
#
# while hours < 24:
#     print(f'{hours} : {minutes} : {seconds}')
#     seconds += 1
#     if seconds > 59:
#         seconds = 0
#         minutes += 1
#         if minutes > 59:
#             minutes = 0
#             hours += 1