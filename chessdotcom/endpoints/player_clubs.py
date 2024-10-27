from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder
from ..utils import from_timestamp


@Client.endpoint
def get_player_clubs(
    username: str, tts=0, **request_options
) -> "GetPlayerClubsResponse":
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
        data = self.serializer.deserialize(text)

        return GetPlayerClubsResponse(
            json={"clubs": data},
            text=text,
            clubs=self._build_clubs(data),
        )

    def _build_clubs(self, data):
        [
            Club(
                id=club.get("id"),
                name=club.get("name"),
                last_activity=club.get("last_activity"),
                icon=club.get("icon"),
                url=club.get("url"),
                joined=club.get("joined"),
            )
            for club in data.get("clubs", [])
        ]


class GetPlayerClubsResponse(ChessDotComResponse):
    def __init__(self, json, text, clubs):
        self.json = json
        self.text = text
        self.clubs = clubs


@dataclass(repr=True)
class Club:
    id: Optional[str]
    name: Optional[str]
    last_activity: Optional[int]
    icon: Optional[str]
    url: Optional[str]
    joined: Optional[int]

    def __post_init__(self):
        self.last_activity_datetime = from_timestamp(self.last_activity)
        self.joined_datetime = from_timestamp(self.joined)
