from task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        pass

    def add_task(self, new_task: Task):
        for t in self.tasks:
            if new_task.name == t.name:
                return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for t in self.tasks:
            if task_name == t.name:
                t.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks_counter = 0
        for t in self.tasks.copy():
            if t.completed:
                completed_tasks_counter += 1
                self.tasks.remove(t)
        return f"Cleared {completed_tasks_counter} tasks."

    def view_section(self):
        template = '\n'.join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n{template}"


# Test Data
# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
