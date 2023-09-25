students_number = int(input())
excellent = 0
very_good = 0
good = 0
fail = 0
total = 0

for _ in range(students_number):
    current_student_grade = float(input())
    total += current_student_grade
    if current_student_grade >= 5:
        excellent += 1
    elif current_student_grade >= 4:
        very_good += 1
    elif current_student_grade >= 3:
        good += 1
    else:
        fail += 1
average = total / students_number
excellent_percentage = excellent / students_number * 100
very_good_percentage = very_good / students_number * 100
good_percentage = good / students_number * 100
fail_percentage = fail / students_number * 100

print(f'Top students: {excellent_percentage:.2f}%')
print(f'Between 4.00 and 4.99: {very_good_percentage:.2f}%')
print(f'Between 3.00 and 3.99: {good_percentage:.2f}%')
print(f'Fail: {fail_percentage:.2f}%')
print(f'Average: {average:.2f}')
