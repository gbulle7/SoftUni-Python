# method 1
last_sector = input()
first_sector_rows = int(input())
seats_odd_row = int(input())
seats_even_row = seats_odd_row + 2
number_seats = 0

for current_sector in range(ord('A'), ord(last_sector) + 1):
    sector = chr(current_sector)
    for current_row in range(1, first_sector_rows + 1):

        if current_row % 2 == 0:
            for seat_even in range(seats_even_row):
                seat = chr(seat_even + ord('a'))
                print(f'{sector}{current_row}{seat}')
                number_seats += 1
        else:
            for seat_odd in range(seats_odd_row):
                seat = chr(seat_odd + ord('a'))
                print(f'{sector}{current_row}{seat}')
                number_seats += 1
    first_sector_rows += 1
print(number_seats)

# method 2 complex
# last_sector = input()
# first_sector_rows = int(input())
# seats_odd_row = int(input())
# seats_even_row = seats_odd_row + 2
# number_seats = 0
#
# for current_sector in range(ord('A'), ord(last_sector) + 1):
#     sector = chr(current_sector)
#     for current_row in range(1, first_sector_rows + 1):
#         seat = (ord('a'))
#         while True:
#             if seats_odd_row <= 0:
#                 seats_odd_row = seats_even_row - 2
#                 break
#             elif seats_even_row <= 0:
#                 seats_even_row = seats_odd_row + 2
#                 break
#             print(f'{sector}{current_row}{chr(seat)}')
#             number_seats += 1
#             seat += 1
#             if current_row % 2 == 0:
#                 seats_even_row -= 1
#                 continue
#             seats_odd_row -= 1
#     first_sector_rows += 1
# print(number_seats)