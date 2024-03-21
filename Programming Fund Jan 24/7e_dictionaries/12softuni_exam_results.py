student_grades = {}
submissions = {}


def max_grade(name, grade):
    if name not in student_grades:
        student_grades[name] = 0
    if grade > student_grades[name]:
        student_grades[name] = grade


def submission(lang):
    if language not in submissions:
        submissions[lang] = 0
    submissions[lang] += 1


def ban(name):
    if name in student_grades:
        del student_grades[name]


while True:
    data = input().split('-')
    username = data[0]
    if username == 'exam finished':
        break
    language = data[1]
    if language == 'banned':
        ban(username)
        continue
    points = int(data[2])
    max_grade(username, points)
    submission(language)

print('Results:')
for student, results in student_grades.items():
    print(f'{student} | {results}')
print('Submissions:')
for subject, entries in submissions.items():
    print(f'{subject} - {entries}')
