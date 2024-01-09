snowballs = int(input())
highest_value = 0
highest_value_weight = 0
highest_value_time = 0
highest_value_quality = 0

for ball in range(snowballs):
    weight = int(input())
    flying_time = int(input())
    quality = int(input())
    value = (weight // flying_time) ** quality
    if value > highest_value:
        highest_value = value
        highest_value_weight = weight
        highest_value_time = flying_time
        highest_value_quality = quality

print(f'{highest_value_weight} : {highest_value_time} = {highest_value} ({highest_value_quality})')