sleep = input()
day = 1
total_distance = 5364

while sleep != 'END':
    if sleep == 'Yes':
        day += 1
    if day > 5:
        break
    climbed_distance = int(input())
    total_distance += climbed_distance
    if total_distance >= 8848:
        break
    sleep = input()
if total_distance >= 8848:
    print(f"Goal reached for {day} days!")
else:
    print("Failed!")
    print(f"{total_distance}")
