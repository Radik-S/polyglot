from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum


class TaskStatus(str, Enum):
    UPLOADING = "UPLOADING"
    READY = "READY"
    PROCESSING = "PROCESSING"
    DONE = "DONE"
    FAILED = "FAILED"


class TaskType(str, Enum):
    AUDIO_TO_TEXT = "AUDIO_TO_TEXT"
    VCF_TO_EXCEL = "VCF_TO_EXCEL"


@dataclass
class Task:
    id: str
    object_key: str
    file_name: str
    status: TaskStatus = TaskStatus.UPLOADING
    updated_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc))
