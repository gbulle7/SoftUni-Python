people = input().split(' ')
kill_index = int(input())
executed = []
counter = 0
person_index = 0

while len(people) > 0:
    counter += 1

    if counter % kill_index == 0:
        executed.append(people.pop(person_index))
    else:
        person_index += 1

    if person_index >= len(people):
        person_index = 0

executed_str = ','.join(executed)
print(f'[{executed_str}]')
