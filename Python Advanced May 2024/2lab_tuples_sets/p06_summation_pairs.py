# import time
sequence = [int(x) for x in input().split()]
target = int(input())

# start = time.time()
targets = set()
values_map = {}

for value in sequence:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        del values_map[value]
        print(f'{pair} + {value} = {target}')
    else:
        result = target - value
        targets.add(result)
        values_map[result] = value
# end = time.time()
# print(f'Time: {end-start}')