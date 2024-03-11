sequence_one = input().split(', ')
sequence_two = input().split(', ')
new_list = []

for substring in sequence_one:
    for string in sequence_two:
        if substring in string and substring not in new_list:
            new_list.append(substring)
            # break
            
print(new_list)
