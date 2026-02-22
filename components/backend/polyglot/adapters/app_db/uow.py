from typing import Optional

from sqlalchemy.orm import Session

from polyglot.application.interfaces import IUnitOfWork

from .repositories import TaskStatusRepo


class SqlAlchemyUnitOfWork(IUnitOfWork):

    def __init__(self, session_factory):
        self._session_factory = session_factory
        self.session: Optional[Session] = None
        self.task_repo = None

    def __enter__(self):
        self.session = self._session_factory()
        self.task_repo = TaskStatusRepo(self.session)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                self.commit()
            else:
                self.rollback()
        finally:
            if self.session is not None:
                self.session.close()

    def commit(self):
        if self.session is not None:
            self.session.commit()

    def rollback(self):
        if self.session is not None:
            self.session.rollback()
