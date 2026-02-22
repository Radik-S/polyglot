from sqlalchemy import Column, DateTime, MetaData, String, Table, func

metadata = MetaData()

task = Table(
    'task',
    metadata,
    Column('id', String, primary_key=True),
    Column('status', String, comment='Статус задачи'),
    Column('object_key', String, comment='Путь до файла в хранилище'),
    Column('file_name', String, comment='Имя файла для обработки'),
    Column('updated_at',
           DateTime(timezone=True),
           nullable=False,
           server_default=func.now(),
           onupdate=func.now(),
           comment='Дата изменения задачи'),
    comment='Задача',
)
