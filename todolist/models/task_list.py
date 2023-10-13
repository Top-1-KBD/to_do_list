from typing import List
from todolist.models.task import Task
from todolist.exceptions.task_exceptions import TaskNotFoundError 

class TaskList:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, name: str, description: str) -> None:
        task = Task(name, description)
        self.tasks.append(task)

    def complete_task(self, task_name: str) -> None:
        for task in self.tasks:
            if task.name == task_name:
                task.mark_as_complete()
                return
        raise TaskNotFoundError("Task not found!")

    def remove_task(self, task_name: str) -> None:
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                return
        raise TaskNotFoundError("Task not found!")

    def display_tasks(self) -> List[str]:
        return [f"{task.name} - {task.description}" for task in self.tasks if not task.completed]