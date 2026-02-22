from typing import Optional

from sqlalchemy import select, update
from sqlalchemy.orm import Session

from polyglot.application.entities import Task, TaskStatus
from polyglot.application.interfaces import ITaskStatusRepo


class TaskStatusRepo(ITaskStatusRepo):

    def __init__(self, session: Session):
        self._session = session

    def add(self, task: Task):
        self._session.add(task)

    def get(self) -> Optional[Task]:
        return self._session.execute(select(Task)).scalars().first()

    def set_status(self, task_id: str, status: TaskStatus) -> bool:
        result = self._session.execute(
            update(Task).where(Task.id == task_id).values(status=status))
        return result.rowcount > 0
