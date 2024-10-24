import json


class ChessDotComError(Exception):
    """
    Custom Exception object.

    :ivar status_code: Contains the status code of the API's response.
    :ivar json: Dictionary representation of the API's response.
    :ivar text: API's raw response decoded into a string.
    """

    def __init__(self, status_code: int, response_text: str, headers: dict) -> None:
        super().__init__()
        self._create_json_attr(response_text)
        self.status_code = status_code
        self.text = response_text
        self.header = headers

    def __str__(self):
        return f"{type(self)}(status_code={self.status_code}, text={self.text})"

    def _create_json_attr(self, response_text: str) -> None:
        try:
            self.json = json.loads(response_text)
        except ValueError:
            self.json = {}
