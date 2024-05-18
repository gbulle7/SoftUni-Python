students_count = int(input())
students = {}

for _ in range(students_count):
    line = tuple(input().split())
    name, grade = line[0], float(line[1])
    if name not in students:
        students[name] = []
    students[name].append(grade)

[print(f'{name} -> {" ".join([f"{g:.2f}" for g in grade])} (avg: {(sum(grade)/len(grade)):.2f})') for name, grade in students.items()]
