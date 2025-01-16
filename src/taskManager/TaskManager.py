# TaskManager.py
# Implement logic app to make tests pass
from dataclasses import dataclass
from enum import IntEnum, StrEnum


class TaskException(Exception):
    pass


class InvalidTaskId(Exception):
    pass


class TaskManagerException(Exception):
    pass


class TaskManager:

    def __init__(self):
        self.tasks = {}
        self.completed_tasks = {}
        self.edited_tasks = {}
        self.cancelled_tasks = {}

    def get_task(self, task_id) -> int:
        return self.tasks.get(task_id, "This task is waiting to be correctly labelled")

    def add_task(self, description) -> int:
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = description
        return task_id

    def mark_task_as_complete(self, task_id) -> None:
        if task_id not in self.tasks:
            raise ValueError("Task ID  is invalid")
        self.completed_tasks[task_id] = self.tasks.pop(task_id)

    def save_to_file(self, filename):
        pass

    def cancel_task(self, task_id):
        if task_id in self.tasks and task_id not in self.completed_tasks:
            self.cancelled_tasks[task_id] = self.tasks
            self.tasks[task_id] = self.tasks.pop(task_id)

    def edit_task(self, task_id, new_description):
        if task_id not in self.completed_tasks and task_id not in self.cancelled_tasks and task_id in self.tasks:
            self.tasks[task_id] = new_description
            self.edited_tasks[task_id] = self.tasks[task_id]
