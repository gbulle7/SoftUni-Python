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


# def process_submission(submissions, username, language, points, number_of_submissions):
#     if language not in number_of_submissions:
#         number_of_submissions[language] = 1
#     else:
#         number_of_submissions[language] += 1
#
#     if username in submissions:
#         if language in submissions[username]:
#             submissions[username][language] = max(submissions[username][language], points)
#         else:
#             submissions[username][language] = points
#     else:
#         submissions[username] = {language: points}
#
#
# def print_results(submissions):
#     print('Results:')
#     for username, languages in submissions.items():
#         max_points = max(languages.values())
#         print(f'{username} | {max_points}')
#
#
# def print_submissions(number_of_submissions):
#     print('Submissions:')
#     for language, count in number_of_submissions.items():
#         print(f'{language} - {count}')
#
#
# submissions = {}
# bans = []
# number_of_submissions = {}
#
# while True:
#     command = input()
#
#     if command == 'exam finished':
#         break
#
#     tokens = command.split('-')
#
#     if len(tokens) == 3:
#         username, language, points = tokens
#         points = int(points)
#         process_submission(submissions, username, language, points, number_of_submissions)
#
#     elif len(tokens) == 2:
#         username, action = tokens
#         if action == 'banned':
#             bans.append(username)
#
#
# for username in bans:
#     if username in submissions:
#         del submissions[username]
#
# print_results(submissions)
# print_submissions(number_of_submissions)



# results = {}
# submissions = {}
# while True:
#     current_result = input().split("-")
#     if len(current_result) == 1:
#         break
#     elif len(current_result) == 2:  # Case where someone is banned
#         name = current_result[0]
#         del results[name]
#     elif len(current_result) == 3:  # else: Case where we got points as input
#         name, current_language, current_points = current_result[0], current_result[1], int(current_result[2])
#         if name not in results.keys():
#             results[name] = 0
#         if results[name] < current_points:
#             results[name] = current_points
#         if current_language not in submissions.keys():
#             submissions[current_language] = 0
#         submissions[current_language] += 1
# print("Results:")
# for username, points in results.items():
#     print(f"{username} | {points}")
# print("Submissions:")
# for language, submissions_count in submissions.items():
#     print(f"{language} - {submissions_count}")