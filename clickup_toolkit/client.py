from enum import Enum
from typing import Union, Literal

import requests

from clickup_toolkit.errors import ClickupApiError
from clickup_toolkit.models import (
    Task,
    UpdateTaskPayload,
    PageMetadata,
    PageData,
)


class RequestMethods(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


ContentFormat = Literal["text/md", "text/plain"]


class ClickUpClient:
    def __init__(self, api_key: str, base_url: str = "https://api.clickup.com/api/v3"):
        self.api_key = api_key
        self.base_url = base_url

    def __get_headers(self):
        return {"Authorization": self.api_key}

    def __make_request(
        self, path: str, method: RequestMethods, payload=None, params=None
    ) -> Union[dict, list, None]:
        response = requests.request(
            method.value,
            path,
            headers=self.__get_headers(),
            json=payload,
            params=params,
        )
        if not response.ok:
            raise ClickupApiError(
                message=response.text, status_code=response.status_code
            )
        return response.json()

    def fetch_task(self, task_id: str) -> Task:
        path = f"{self.base_url}/task/{task_id}"
        response = self.__make_request(
            method=RequestMethods.GET,
            path=path,
        )
        return Task(**response)

    def update_task(self, task_id: str, update_task_payload: UpdateTaskPayload) -> Task:
        path = f"{self.base_url}/task/{task_id}"
        response = self.__make_request(
            path,
            method=RequestMethods.PUT,
            payload=update_task_payload.model_dump(exclude_none=True),
        )
        return Task(**response)

    def get_doc_listing(self, workspace_id: int, doc_id: str) -> list[PageMetadata]:
        path = f"{self.base_url}/workspaces/{workspace_id}/docs/{doc_id}/pageListing"
        response = self.__make_request(
            path=path,
            method=RequestMethods.GET,
        )
        assert isinstance(response, list)
        return [PageMetadata(**el) for el in response]

    def get_page(
        self,
        workspace_id: int,
        doc_id: str,
        page_id: str,
        content_format: ContentFormat = "text/md",
    ) -> PageData:
        path = (
            f"{self.base_url}/workspaces/{workspace_id}/docs/{doc_id}/pages/{page_id}"
        )
        params = {"content_format": content_format}
        response = self.__make_request(
            path=path,
            method=RequestMethods.GET,
            params=params,
        )
        return PageData(**response)
