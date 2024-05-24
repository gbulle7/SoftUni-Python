line = [[x.strip() for x in sublist.split()] for sublist in input().split('|')]
flattened_list = []
while line:
    current_list = line.pop()
    flattened_list.extend(current_list)
print(*flattened_list)
