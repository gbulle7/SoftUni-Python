from project.person import Person
from project.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."


# teacher = Teacher()
# print(teacher.sleep())
# print(teacher.get_fired())
# print(teacher.teach())
