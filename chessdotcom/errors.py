import json

from chessdotcom.types import BaseType

class ChessDotComError(BaseType, Exception):
    """
    Custom Exception object.

    :ivar status_code: Contains the status code of the API's response.
    :ivar json: Dictionary representation of the API's response.
    :ivar text: API's raw response decoded into a string.
    """

    def __init__(self, status_code: int, response_text: str) -> None:
        super().__init__(self)
        self._create_json_attr(response_text)
        self.status_code = status_code
        self.text = response_text

    def _create_json_attr(self, response_text: str) -> None:
        try: self.json = json.loads(response_text)
        except: self.json = {}
