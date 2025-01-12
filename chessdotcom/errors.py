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
    :ivar headers: Contains the headers of the API's response.
    :ivar url: The URL that caused the error.
    """

    def __init__(
        self, status_code: int, response_text: str, headers: dict, json: dict, url: str
    ) -> None:
        super().__init__()
        self.json = json
        self.status_code = status_code
        self.text = response_text
        self.headers = headers
        self.url = url

    def __str__(self):
        return (
            "ChessDotComClientError("
            f"status_code={self.status_code}, "
            f"text={self.text}, "
            f"url={self.url})"
        )


class ChessDotComDecodingError(ChessDotComError):
    """
    Error raised when the response cannot be decoded.
    """

    def __init__(self, text, *args: object) -> None:
        self.text = text
        super().__init__(*args)
