sequence = list(map(int, input().split()))
# sequence = [int(i) for i in input().split()]
left_car_time = 0
right_car_time = 0
halved = len(sequence) // 2

for step in range(halved):
    left_car_time += sequence[step]
    if sequence[step] == 0:
        left_car_time *= 0.8
sequence.reverse()
for step in range(halved):
    right_car_time += sequence[step]
    if sequence[step] == 0:
        right_car_time *= 0.8
if right_car_time < left_car_time:
    winner = 'right'
    time = right_car_time
else:
    winner = 'left'
    time = left_car_time

print(f'The winner is {winner} with total time: {time:.1f}')
