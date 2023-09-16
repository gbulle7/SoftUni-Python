total_steps = 0
target_steps = 10000

while total_steps < target_steps:
    current_steps = input()
    if current_steps == 'Going home':
        current_steps = int(input())
        total_steps += current_steps
        break
    total_steps += int(current_steps)
difference = abs(total_steps - target_steps)
if total_steps >= target_steps:
    print('Goal reached! Good job!')
    print(f'{difference} steps over the goal!')
else:
    print(f'{difference} more steps to reach goal.')