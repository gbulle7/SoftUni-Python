from math import floor

w = float(input())      # length of classroom
h = float(input())      # width of classroom
seat_length = 1.2
seat_width = 0.7
number_rows = floor(w / seat_length)
number_columns = floor((h - 1) / seat_width)
number_seats = number_rows * number_columns - 3  # 3 seats less because of door and podium taking up space
print(floor(number_seats))
