from typing import Dict
from chessdotcom.errors import ChessDotComError
import json

class ChessDotComResponse(object):
    """Custom object for holding the API's response."""

    def __init__(self, response_data: Dict) -> None:
        self._response_data = self._parse_json(response_data)

    @staticmethod
    def _parse_json(response_data):
        try:
            data = json.loads(response_data.decode('utf-8'))
        except Exception as exc:
            raise ChessDotComError(
                status_code = 200,
                message = 'The API returned 200, but the response was provided in an invalid format'
            ) from exc
        else:
            return data

    @property
    def json(self):
        """
        :returns: The data from the Chess.com API's response in dictionary format.
        """
        return self._response_data
