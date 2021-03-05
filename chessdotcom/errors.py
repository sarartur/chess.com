import json

class ChessDotComError(Exception):
    """
    Custom Exception object.

    :ivar status_code: Contains the status code of the API's response.
    :ivar json: Dictionary representation of the API's response
    """

    def __init__(self, status_code, response_text):
        super().__init__(self)
        self.json = json.loads(response_text)
        self.status_code = status_code

    def __str__(self):
        return (
            f"ChessDotComError(status_code={self.status_code}, "
                            f"json={self.json})"
        )

    def __repr__(self):
        return self.__str__()