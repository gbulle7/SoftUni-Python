students_data = {}
info = input()

while ':' in info:
    student_name, student_id, course = info.split(':')      # = info[0], info[1], info[2];  If "id" as number-> int(info[1])
    if course not in students_data:
        students_data[course] = {}
    students_data[course][student_id] = student_name
    info = input()

filter_course = ' '.join(info.split('_'))

for key, value in students_data.items():
    if key == filter_course:
        for student_id, student_name in value.items():
            print(f'{student_name} - {student_id}')


# student_information = input()
# students = {}
#
# while not students.get(student_information):
#     student_information = student_information.split(":")
#     name = student_information[0]
#     id = student_information[1]
#     course = student_information[-1]
#
#     if course not in students:
#         students[course] = {}
#     students[course][name] = id
#     student_information = input()
#     student_information = student_information.replace("_", " ")
#
# for key, value in students[student_information].items():
#     print(f"{key} - {value}")