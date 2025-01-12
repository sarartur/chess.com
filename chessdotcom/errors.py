class ChessDotComError(Exception):
    """
    Base Exception object.
    """

    pass


class ChessDotComClientError(ChessDotComError):
    """
    Error raised by Client.

    :ivar status_code: Contains the status code of the API's response.
    :ivar json: Dictionary representation of the API's response.
    :ivar text: API's raw response decoded into a string.
    """

    def __init__(
        self, status_code: int, response_text: str, headers: dict, json
    ) -> None:
        super().__init__()
        self.json = json
        self.status_code = status_code
        self.text = response_text
        self.headers = headers

    def __str__(self):
        return f"{type(self)}(status_code={self.status_code}, text={self.text})"


class ChessDotComDecodingError(ChessDotComError):
    """
    Error raised when the response cannot be decoded.
    """

    def __init__(self, text, *args: object) -> None:
        self.text = text
        super().__init__(*args)
