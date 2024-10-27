from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder


@Client.endpoint
def get_player_clubs(username: str, tts=0, **request_options) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
            a list of clubs the player is a member of.
    """
    return Resource(
        uri=f"/player/{username}/clubs", tts=tts, request_options=request_options
    )


class ResponseBuilder(ResponseBuilder):
    def build(self, text):
        pass


class GetPlayerClubsResponse(ChessDotComResponse):
    def __init__(self, json, text, clubs):
        self.json = json
        self.text = text
        self.clubs = clubs


@dataclass
@dataclass
class Club:
    id: Optional[str] = None
    name: Optional[str] = None
    last_activity: Optional[int] = None
    icon: Optional[str] = None
    url: Optional[str] = None
    joined: Optional[int] = None
