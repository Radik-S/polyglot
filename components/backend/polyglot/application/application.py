import uuid
from typing import Callable, Tuple

from polyglot.application.entities import Task, TaskStatus
from polyglot.application.interfaces import IObjectStorage, IUnitOfWork


class TaskService:

    def __init__(
        self,
        object_storage: IObjectStorage,
        uow_factory: Callable[[], IUnitOfWork],
    ):
        self.object_storage = object_storage
        self.uow_factory = uow_factory

    def create_task(self, filename) -> Task:
        task_id = str(uuid.uuid4())
        object_key = f"{task_id}/{filename}"
        task = Task(id=task_id, object_key=object_key, file_name=filename)
        with self.uow_factory() as uow:
            uow.task_repo.add(task)
        return task

    def set_task_status(self, task_id: str, status: TaskStatus) -> bool:
        with self.uow_factory() as uow:
            return uow.task_repo.set_status(task_id, status)
