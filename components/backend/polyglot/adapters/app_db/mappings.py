from sqlalchemy.orm import registry, relationship

from polyglot.application import entities

from . import tables

mapper = registry()

mapper.map_imperatively(
    entities.Task,
    tables.task,
)
