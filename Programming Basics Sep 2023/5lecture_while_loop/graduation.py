student_name = input()
year = 1
total_score = 0
failed_class = 0

while year <= 12:
    current_score = float(input())
    if current_score < 4:
        failed_class += 1
        if failed_class > 1:
            print(f'{student_name} has been excluded at {year} grade')
            break
        continue
    year += 1
    total_score += current_score
else:
    average_score = total_score / 12
    print(f'{student_name} graduated. Average grade: {average_score:.2f}')


# with while true
#
# student_name = input()
# year = 1
# total_score = 0
# failed_class = 0
#
# while True:
#     if year <= 12:
#         current_score = float(input())
#         if current_score < 4:
#             failed_class += 1
#             if failed_class > 1:
#                 print(f'{student_name} has been excluded at {year} grade')
#                 break
#             continue
#         year += 1
#         total_score += current_score
#     else:
#         average_score = total_score / 12
#         print(f'{student_name} graduated. Average grade: {average_score:.2f}')
#         break
