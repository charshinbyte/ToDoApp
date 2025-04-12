from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

def current_timestamp() -> int:
    return int(datetime.now().timestamp())

# Input model — used in POST requests
class TaskCreate(BaseModel):
    title: str

# Internal model — includes timestamps
class Task(TaskCreate):
    is_completed: bool = False
    is_deleted: bool = False
    updated_at: int = Field(default_factory=current_timestamp)
    creation: int = Field(default_factory=current_timestamp)


class TaskOut(BaseModel):
    id: str
    title: str
    is_completed: bool = False
    is_deleted: bool = False
    updated_at: int = Field(default_factory=current_timestamp)
    creation: int = Field(default_factory=current_timestamp)