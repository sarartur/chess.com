import json
import re
from types import SimpleNamespace

from multidict import CIMultiDictProxy


class Collection(SimpleNamespace):
    def __init__(self, **kwargs) -> None:
        clean_kwargs = {Collection.clean(key): value for key, value in kwargs.items()}
        SimpleNamespace.__init__(self, **clean_kwargs)

    @staticmethod
    def clean(string: str) -> str:
        string = re.sub("[^0-9a-zA-Z_]", "", re.sub("^[^a-zA-Z_]+", "", string))
        return string


class BaseType(object):
    def __init__(self) -> None:
        pass

    _exclude_from_str = ["json", "text"]

    def __str__(self) -> str:
        items = (
            f"{k}={v!r}"
            for k, v in self.__dict__.items()
            if k not in self.__class__._exclude_from_str
        )
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __repr__(self) -> str:
        items = (f"{k}={v!r}" for k, v in self.__dict__.items())
        return "{}({})".format(type(self).__name__, ", ".join(items))


class ChessDotComResponse(BaseType):
    """
    Custom object for holding the API's response.

    :ivar json: Dictionary representation of the API's response.
    :ivar {nested_object}: Object representation of the API's response.
    :ivar text: API's raw response decoded into a string.
    """

    def __init__(
        self, response_text: str, top_level_attribute: str = None, no_json=False
    ) -> None:
        self._parse_response(response_text, top_level_attribute, no_json)
        self.text = response_text

    def _parse_response(
        self, response_text: str, top_level_attribute: str, no_json
    ) -> None:
        if no_json:
            response_text = json.dumps({top_level_attribute: response_text})
        try:
            self._create_json_attr(response_text, top_level_attribute)
            self._create_object_attrs(response_text, top_level_attribute)
        except Exception as err:
            raise ChessDotComError(
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
        attrs = json.loads(response_text, object_hook=lambda d: Collection(**d))
        if top_level_attribute:
            setattr(self, top_level_attribute, Collection(**attrs.__dict__))
        else:
            self.__dict__.update(**attrs.__dict__)


class ChessDotComError(Exception):
    """
    Custom Exception object.

    :ivar status_code: Contains the status code of the API's response.
    :ivar json: Dictionary representation of the API's response.
    :ivar text: API's raw response decoded into a string.
    """

    def __init__(
        self, status_code: int, response_text: str, headers: CIMultiDictProxy
    ) -> None:
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
