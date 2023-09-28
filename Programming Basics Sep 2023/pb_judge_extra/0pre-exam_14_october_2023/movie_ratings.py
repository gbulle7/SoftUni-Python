movie_number = int(input())
max_rating = float('-inf')
min_rating = float('inf')
total_rating = 0
max_rating_movie = ''
min_rating_movie = ''


for movie in range(movie_number):
    movie_name = input()
    movie_rating = float(input())
    if movie_rating > max_rating:
        max_rating = movie_rating
        max_rating_movie = movie_name
    if movie_rating < min_rating:
        min_rating = movie_rating
        min_rating_movie = movie_name
    total_rating += movie_rating
average_rating = total_rating / movie_number

print(f"{max_rating_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_rating_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")