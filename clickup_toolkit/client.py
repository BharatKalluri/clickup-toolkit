from enum import Enum

import requests

from clickup_toolkit.errors import ClickupApiError
from clickup_toolkit.models import Task, UpdateTaskPayload


class RequestMethods(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class ClickUpClient:
    def __init__(self, api_key: str, base_url: str = "https://api.clickup.com/api/v2"):
        self.api_key = api_key
        self.base_url = base_url

    def __get_headers(self):
        return {"Authorization": self.api_key}

    def __make_request(self, path: str, method: RequestMethods, payload=None):
        response = requests.request(
            method.value, path, headers=self.__get_headers(), json=payload
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
        if not response.ok:
            raise ClickupApiError(
                message=response.text, status_code=response.status_code
            )
        return Task(**response.json())

    def update_task(self, task_id: str, update_task_payload: UpdateTaskPayload) -> Task:
        path = f"{self.base_url}/task/{task_id}"
        response = requests.put(
            path,
            headers=self.__get_headers(),
            json=update_task_payload.model_dump(exclude_none=True),
        )
        if not response.ok:
            raise ClickupApiError(
                message=response.text, status_code=response.status_code
            )
        return Task(**response.json())
