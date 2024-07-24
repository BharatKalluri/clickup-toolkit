from typing import Optional, List

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

    text_content: Optional[str]
    description: Optional[str]

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


class FetchAllTasksPayload(BaseModel):
    archived: Optional[bool] = None
    include_markdown_description: Optional[bool] = None
    page: Optional[int] = None
    order_by: Optional[str] = None
    reverse: Optional[bool] = None
    subtasks: Optional[bool] = None
    statuses: Optional[List[str]] = None
    include_closed: Optional[bool] = None
    assignees: Optional[List[str]] = None
    watchers: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    due_date_gt: Optional[int] = None
    due_date_lt: Optional[int] = None
    date_created_gt: Optional[int] = None
    date_created_lt: Optional[int] = None
    date_updated_gt: Optional[int] = None
    date_updated_lt: Optional[int] = None
    date_done_gt: Optional[int] = None
    date_done_lt: Optional[int] = None
    custom_fields: Optional[List[str]] = None
    custom_field: Optional[List[str]] = None
    custom_items: Optional[List[int]] = None


class FetchAllTasksResponse(BaseModel):
    tasks: List[Task]
    last_page: bool


class DeleteTaskPayload(BaseModel):
    custom_task_ids: Optional[bool] = None
    team_id: Optional[float] = None
