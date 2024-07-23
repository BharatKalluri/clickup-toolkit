from typing import Optional

from pydantic import BaseModel


class Status(BaseModel):
    id: Optional[str] = None
    status: str
    color: Optional[str] = None

    orderindex: Optional[int] = None

    type: Optional[str] = None


class Task(BaseModel):
    id: str
    custom_id: Optional[str] = None
    name: Optional[str] = None

    text_content: str
    description: str

    status: Optional[Status] = None

    orderindex: Optional[str] = None
    date_created: Optional[int] = None
    date_updated: Optional[int] = None
    date_closed: Optional[int] = None

    due_date: Optional[str] = None
    start_date: Optional[str] = None

    url: str


class UpdateTaskPayload(BaseModel):
    status: Optional[str] = None
    start_date: Optional[int] = None
    due_date: Optional[int] = None
