movie_name = input()
days = int(input())
tickets_number = int(input())
tickets_price  = float(input())
percent_for_cinema = int(input())

total_price = tickets_price * tickets_number * days
revenue = total_price * (1 - percent_for_cinema * 0.01)

print(f'The profit from the movie {movie_name} is {revenue:.2f} lv.')