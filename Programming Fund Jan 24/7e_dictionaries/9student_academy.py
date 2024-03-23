number_students = int(input())
students = {}

for _ in range(number_students):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)

for student in students:
    students[student] = sum(students[student]) / len(students[student])
# students_above_average = {name: sum(grades) / len(grades) for name, grades in students.items()
#                           if sum(grades) / len(grades) >= 4.50}

# passing_students = students.copy()
for student, average_grade in students.items():
    if average_grade < 4.5:
        continue
        # passing_students.pop(student)
    else:
        print(f'{student} -> {average_grade:.2f}')
