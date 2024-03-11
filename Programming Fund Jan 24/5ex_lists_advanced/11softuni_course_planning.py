schedule = input().split(', ')
command = input()

while command != 'course start':
    command = command.split(':')
    cmd = command[0]
    lesson = command[1]
    exercise = f'{lesson}-Exercise'

    if cmd == 'Add':
        if lesson not in schedule:
            schedule.append(lesson)
    elif cmd == 'Insert':
        if lesson not in schedule:
            schedule.insert(int(command[2]), lesson)
    elif cmd == 'Remove':
        if lesson in schedule:
            schedule.remove(lesson)
        if exercise in schedule:
            schedule.remove(exercise)
    elif cmd == 'Swap':
        title_two = command[2]
        exercise_two = f'{title_two}-Exercise'
        if lesson in schedule and title_two in schedule:
            les1 = schedule.index(lesson)
            les2 = schedule.index(title_two)
            schedule[les1], schedule[les2] = schedule[les2], schedule[les1]
        if exercise in schedule:
            lesson_index = schedule.index(lesson)
            schedule.remove(exercise)
            schedule.insert(lesson_index + 1, exercise)
        if exercise_two in schedule:
            title_index = schedule.index(title_two)
            schedule.remove(exercise_two)
            schedule.insert(title_index + 1, exercise_two)
    elif cmd == 'Exercise':
        if lesson in schedule and exercise not in schedule:
            lesson_index = schedule.index(lesson)
            schedule.insert(lesson_index + 1, exercise)
        elif lesson not in schedule:
            schedule.append(lesson)
            schedule.append(exercise)

    command = input()

for indx, title in enumerate(schedule):
    print(f'{indx + 1}.{title}')

# To Do the task using Functions...