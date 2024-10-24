import json
import re
from types import SimpleNamespace

from .errors import ChessDotComClientError


class ResponseBuilder(object):
    def build(self, text):
        raise NotImplementedError("Method must be defined by the child class")


class DefaultResponseBuilder(ResponseBuilder):
    def __init__(self, resource) -> None:
        self.resource = resource

    def build(self, text):
        return ChessDotComResponse(
            text=text,
            top_level_attribute=self.resource.top_level_attribute,
            no_json=self.resource.no_json,
        )


class ChessDotComResponse(object):
    """
    Object for holding the API's response.

    :ivar json: Dictionary representation of the API's response.
    :ivar {nested_object}: Object representation of the API's response.
    :ivar text: API's raw response decoded into a string.
    """

    def __init__(
        self, text: str, top_level_attribute: str = None, no_json=False
    ) -> None:
        self._parse_response(text, top_level_attribute, no_json)
        self.text = text

    def _parse_response(
        self, response_text: str, top_level_attribute: str, no_json
    ) -> None:
        if no_json:
            response_text = json.dumps({top_level_attribute: response_text})
        try:
            self._create_json_attr(response_text, top_level_attribute)
            self._create_object_attrs(response_text, top_level_attribute)
        except Exception as err:
            raise ChessDotComClientError(
                status_code=200,
                response_text=json.dumps(
                    {
                        "message": "The server did not return a json response",
                    }
                ),
            ) from err

    def _create_json_attr(self, response_text: str, top_level_attribute: str) -> None:
        dict_ = json.loads(response_text)
        if top_level_attribute:
            dict_ = {top_level_attribute: dict_}
        self.json = dict_

    def _create_object_attrs(
        self, response_text: str, top_level_attribute: str
    ) -> None:
        attrs = json.loads(response_text, object_hook=lambda d: Entity(**d))
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
