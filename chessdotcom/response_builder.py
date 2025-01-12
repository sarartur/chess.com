import json
import re
from types import SimpleNamespace

from .errors import ChessDotComClientError, ChessDotComDecodingError


class ResponseBuilder(object):
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


class DefaultResponseBuilder(ResponseBuilder):
    def build(self, text):
        return ChessDotComResponse(
            text=text,
            top_level_attribute=self.resource.top_level_attribute,
        )


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
    Object for holding the API's response.

    :ivar json: Dictionary representation of the API's response.
    :ivar {nested_object}: Object representation of the API's response.
    :ivar text: API's raw response decoded into a string.
    """

    def __init__(self, text: str, top_level_attribute: str = None) -> None:
        self.text = text
        self._parse_text(top_level_attribute)

    def _parse_text(self, top_level_attribute: str) -> None:
        try:
            self._create_json_attr(top_level_attribute)
            self._create_object_attrs(top_level_attribute)
        except Exception as err:
            raise ChessDotComDecodingError(
                self.text, "Response could not be converted to JSON"
            ) from err

    def _create_json_attr(self, top_level_attribute: str) -> None:
        dict_ = json.loads(self.text)
        if top_level_attribute:
            dict_ = {top_level_attribute: dict_}
        self.json = dict_

    def _create_object_attrs(self, top_level_attribute: str) -> None:
        attrs = json.loads(self.text, object_hook=lambda d: Entity(**d))
        if top_level_attribute:
            setattr(self, top_level_attribute, Entity(**attrs.__dict__))
        else:
            self.__dict__.update(**attrs.__dict__)

    def __repr__(self) -> str:
        items = (
            f"{k}={v!r}" for k, v in self.__dict__.items() if k not in ["json", "text"]
        )
        return "{}({})".format(type(self).__name__, ", ".join(items))


class Entity(SimpleNamespace):
    def __init__(self, **kwargs) -> None:
        clean_kwargs = {self._clean_key(key): value for key, value in kwargs.items()}
        SimpleNamespace.__init__(self, **clean_kwargs)

    def _clean_key(self, string: str) -> str:
        string = re.sub("[^0-9a-zA-Z_]", "", re.sub("^[^a-zA-Z_]+", "", string))
        return string
