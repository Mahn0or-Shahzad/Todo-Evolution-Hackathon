from typing import List, Optional
from datetime import datetime
from todo_model import TodoTask

class TodoStore:
    def __init__(self):
        self._tasks: List[TodoTask] = []
        self._next_id: int = 1

    def get_all(self) -> List[TodoTask]:
        return self._tasks

    def get_by_id(self, task_id: int) -> Optional[TodoTask]:
        return next((task for task in self._tasks if task.id == task_id), None)

    def add_task(self, title: str, description: Optional[str] = None) -> TodoTask:
        if not title.strip():
            raise ValueError("Task title cannot be empty.")

        task = TodoTask(
            id=self._next_id,
            title=title.strip(),
            description=description,
            created_at=datetime.now()
        )
        self._tasks.append(task)
        self._next_id += 1
        return task

    def delete_task(self, task_id: int) -> bool:
        task = self.get_by_id(task_id)
        if task:
            self._tasks.remove(task)
            return True
        return False

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        task = self.get_by_id(task_id)
        if not task:
            return False

        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty.")
            task.title = title.strip()

        if description is not None:
            task.description = description

        return True

    def toggle_completion(self, task_id: int) -> bool:
        task = self.get_by_id(task_id)
        if task:
            task.is_completed = not task.is_completed
            return True
        return False
