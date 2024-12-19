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


class PageMetadata(BaseModel):
    id: str
    doc_id: str
    parent_page_id: Optional[str] = None
    workspace_id: int
    name: str
    pages: Optional[list["PageMetadata"]] = []


class UpdateTaskPayload(BaseModel):
    status: Optional[str] = None
    start_date: Optional[int] = None
    due_date: Optional[int] = None


class PageData(BaseModel):
    id: str
    doc_id: str
    parent_page_id: Optional[str] = None
    workspace_id: int
    name: str
    pages: Optional[List["PageData"]] = None
    sub_title: Optional[str] = None
    date_created: Optional[int] = None
    date_updated: Optional[int] = None
    content: Optional[str] = None
    creator_id: Optional[int] = None
    deleted: Optional[bool] = None
    deleted_by: Optional[int] = None
    date_deleted: Optional[int] = None
    date_edited: Optional[int] = None
    edited_by: Optional[int] = None
    archived: Optional[bool] = None
    archived_by: Optional[int] = None
    date_archived: Optional[int] = None
    authors: Optional[List[int]] = None
    contributors: Optional[List[int]] = None
    protected: Optional[bool] = None
    protected_by: Optional[int] = None
    protected_note: Optional[str] = None
