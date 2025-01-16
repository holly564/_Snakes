# TaskManager.py
from dataclasses import dataclass, field
from enum import IntEnum, StrEnum


class Task_status(StrEnum):
    DEFAULT_STATUS = 'default',
    COMPLETED = 'completed',
    CANCELLED = 'cancelled',
    EDITED = 'edited'


@dataclass(frozen=True, order=True)
class Task:
    id: int = 0
    description: str = ""
    status: Task_status = Task_status.DEFAULT_STATUS


class TaskException(Exception):
    pass


class InvalidTaskId(Exception):
    pass


class TaskManagerException(Exception):
    pass


class ImprovedTaskManager:

    def __init__(self):
        self.tasks: list[Task] = []
        self.completed_tasks : list[Task] = []
        self.edited_tasks: list[Task] = []
        self.cancelled_tasks: list[Task] = []

    def get_task(self, task_id) -> int:

        self.tasks.__add__(Task (task_id, "reer", Task_status.EDITED))
        self.tasks.append(task_id, "This task is waiting to be correctly labelled", )
        self.tasks.pop()
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
