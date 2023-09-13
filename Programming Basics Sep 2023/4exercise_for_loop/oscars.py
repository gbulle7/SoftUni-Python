actor_name = input()
starting_points = float(input())
jury_number = int(input())
additional_points = 0

for _ in range(jury_number):
    jury_name = input()
    jury_points = float(input())
    additional_points += len(jury_name) * jury_points / 2
    if additional_points + starting_points >= 1250.5:
        total_points = additional_points + starting_points
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        break
else:
    needed_points = 1250.5 - (additional_points + starting_points)
    print(f'Sorry, {actor_name} you need {needed_points:.1f} more!')
