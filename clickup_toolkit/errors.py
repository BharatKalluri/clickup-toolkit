class ClickupApiError(Exception):
    """Raised when an API call to Clickup fails."""

    def __init__(self, message: str, status_code: int) -> None:
        super().__init__(message)
        self.status_code = status_code
