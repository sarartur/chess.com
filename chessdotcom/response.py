from typing import Dict
from types import SimpleNamespace
import json

from chessdotcom.errors import ChessDotComError
from chessdotcom.types import Collection

class ChessDotComResponse(object):
    """
    Custom object for holding the API's response.

    :ivar json: Dictionary representation of the API's response
    :ivar {nested_object}: Object representation of the API's response
    """

    def __init__(self, response_data: Dict, top_level_attr = None) -> None:
        self._parse_response(response_data, top_level_attr)

    def __repr__(self):
        attrs_string = ''
        for name, attr in self.__dict__.items():
            if name == 'json':
                continue
            attrs_string += f"{name}={attr}, "
        return (
            f"ChessDotComResponse({attrs_string.strip(', ')})"
        )
        
    def _parse_response(self, response_data, top_level_attr):
        try:
            self._create_json_attr(response_data, top_level_attr)
            self._create_object_attrs(response_data, top_level_attr)
        except Exception as err:
            raise ChessDotComError(
                status_code = 200,
                message = 'The API returned 200, but the response was provided in an invalid format'
            ) from err
            
    def _create_json_attr(self, response_data, top_level_attr):
        dict_ = json.loads(response_data.decode('utf-8'))
        if top_level_attr:
            dict_ = {top_level_attr: dict_}
        self.json = dict_

    def _create_object_attrs(self, response_data, top_level_attr):
        attrs = json.loads(response_data.decode('utf-8'), object_hook=lambda d: Collection(**d))
        if top_level_attr:
            setattr(self, top_level_attr, Collection(**attrs.__dict__))
        else:
            self.__dict__.update(**attrs.__dict__)

