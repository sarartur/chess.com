import json

from .errors import ChessDotComClientError, ChessDotComDecodingError


class BaseResponseBuilder(object):
    def __init__(self, serializer=None) -> None:
        self.serializer = serializer or Serializer()

    def build(self, text):
        raise NotImplementedError("Method must be defined by the child class")

    def build_client_error(self, status_code: int, response_text: str, headers: dict):
        return ChessDotComClientError(
            status_code=status_code,
            response_text=response_text,
            headers=headers,
            json=self._build_json(response_text),
            url=self.resource.url,
        )

    def register_resource(self, resource):
        self.resource = resource

    def _build_json(self, response_text: str):
        try:
            return self.serializer.deserialize(response_text)
        except ChessDotComDecodingError:
            return {}


class DefaultResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        return ChessDotComResponse(text=text, json=self._build_json(text))


class Serializer(object):
    def deserialize(self, text):
        try:
            data = json.loads(text)
        except json.JSONDecodeError as err:
            raise ChessDotComDecodingError(
                text, "Response could not be converted to JSON"
            ) from err

        return data


class ChessDotComResponse(object):
    """
    Base object for holding the API's response.

    :ivar json: Dictionary representation of the API's response.
    :ivar text: API's raw response decoded into a string.
    """

    def __init__(self, text: str, json) -> None:
        self.text = text
        self.json = json
