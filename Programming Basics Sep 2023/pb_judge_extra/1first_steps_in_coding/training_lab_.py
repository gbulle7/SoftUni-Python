w = float(input())      # length of classroom
h = float(input())      # width of classroom including corridor
classroom_width = h - 1     # 1 m empty for corridor
seats_per_rows = int(classroom_width / 0.7)  # 0.7 m width of seat
seats_per_columns = int(w / 1.2)  # 1.2 m length of seat
number_seats = seats_per_rows * seats_per_columns - 3  # 3 seats less because of door and podium taking up space
print(number_seats)