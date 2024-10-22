class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
        else:
            print("Неверный индекс задачи.")

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def __str__(self):
        if not self.tasks:
            return "Нет задач."
        return "\n".join(str(task) for task in self.tasks)

# Пример использования
task_manager = TaskManager()
task_manager.add_task("Сделать домашнее задание", "2024-10-18")
task_manager.add_task("Купить продукты", "2024-10-26")

print("Все задачи:")
print(task_manager)

task_manager.mark_task_as_completed(0)

print("\nТекущие задачи:")
for task in task_manager.get_current_tasks():
    print(task)