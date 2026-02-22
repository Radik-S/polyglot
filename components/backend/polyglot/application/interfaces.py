from abc import ABC, abstractmethod
from typing import Optional

from polyglot.application.entities import Task, TaskStatus


class ITaskStatusRepo(ABC):

    @abstractmethod
    def add(self, task: Task):
        ...

    @abstractmethod
    def get(self) -> Optional[Task]:
        ...

    @abstractmethod
    def set_status(self, task_id: str, status: TaskStatus) -> bool:
        ...


class IUnitOfWork(ABC):
    task_repo: ITaskStatusRepo

    @abstractmethod
    def __enter__(self):
        ...

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        ...

    @abstractmethod
    def commit(self):
        ...

    @abstractmethod
    def rollback(self):
        ...


class IObjectStorage(ABC):

    @abstractmethod
    def generate_presigned_url(self, object_key: str,
                               content_type: str) -> str:
        """Генерирует ссылку для загрузки файла."""
        ...
