# method 1
maximum_fails = int(input())
task_name = input()
task_number = 0
total_score = 0
failed_grades = 0
last_task = ''

while task_name != 'Enough':
    current_score = int(input())
    if current_score <= 4:
        failed_grades += 1
        if failed_grades >= maximum_fails:
            print(f'You need a break, {failed_grades} poor grades.')
            break
    total_score += current_score
    task_number += 1
    last_task = task_name
    task_name = input()
else:
    average_score = total_score / task_number
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {task_number}')
    print(f'Last problem: {last_task}')

# # method 2
# maximum_fails = int(input())
# task_number = 0
# total_score = 0
# failed_grades = 0
# last_task = ''
# has_failed = True
#
# while failed_grades < maximum_fails:
#     task_name = input()
#     if task_name == 'Enough':
#         has_failed = False
#         break
#     current_score = int(input())
#     if current_score <= 4:
#         failed_grades += 1
#     total_score += current_score
#     task_number += 1
#     last_task = task_name
# if has_failed:
#     print(f'You need a break, {failed_grades} poor grades.')
# else:
#     average_score = total_score / task_number
#     print(f'Average score: {average_score:.2f}')
#     print(f'Number of problems: {task_number}')
#     print(f'Last problem: {last_task}')
