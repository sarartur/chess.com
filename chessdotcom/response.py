import json

from chessdotcom.errors import ChessDotComError
from chessdotcom.types import Collection, BaseType

class ChessDotComResponse(BaseType):
    """
    Custom object for holding the API's response.

    :ivar json: Dictionary representation of the API's response.
    :ivar {nested_object}: Object representation of the API's response.
    :ivar text: API's raw response decoded into a string.
    """

    def __init__(self, response_text: str, top_level_attr: str = None) -> None:
        self._parse_response(response_text, top_level_attr)
        self.text = response_text

    def _parse_response(self, response_text: str, top_level_attr: str) -> None: 
        try:
            self._create_json_attr(response_text, top_level_attr)
            self._create_object_attrs(response_text, top_level_attr)
        except Exception as err:
            raise ChessDotComError(
                status_code = 200,
                response_text = json.dumps({
                    "message": "The server did not return a json response",
                })
            ) from err
            
    def _create_json_attr(self, response_text: str, top_level_attr: str) -> None:
        dict_ = json.loads(response_text)
        if top_level_attr:
            dict_ = {top_level_attr: dict_}
        self.json = dict_

    def _create_object_attrs(self, response_text: str, top_level_attr: str) -> None:
        attrs = json.loads(response_text, object_hook=lambda d: Collection(**d))
        if top_level_attr:
            setattr(self, top_level_attr, Collection(**attrs.__dict__))
        else:
            self.__dict__.update(**attrs.__dict__)


