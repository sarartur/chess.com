"""
List of clubs the player is a member of, with joined date and last activity date.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-player-clubs
"""


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
    :returns: :obj:`GetPlayerClubsResponse` object containing
            a list of clubs the player is a member of.
    """
    return Resource(
        uri=f"/player/{username}/clubs",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
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
        return [
            Club(
                id=club.get("@id"),
                name=club.get("name"),
                last_activity=club.get("last_activity"),
                icon=club.get("icon"),
                url=club.get("url"),
                joined=club.get("joined"),
            )
            for club in data.get("clubs", [])
        ]


class GetPlayerClubsResponse(ChessDotComResponse):
    """
    :ivar clubs: Holds an array of :obj:`Club` objects.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json, text, clubs):
        self.json = json
        self.text = text
        self.clubs = clubs


@dataclass(repr=True)
class Club:
    """
    :ivar id: The unique identifier of the club.
    :ivar name: The name of the club.
    :ivar last_activity: The timestamp of the last activity in the club.
    :ivar icon: The URL of the club's icon.
    :ivar url: The URL of the club's page.
    :ivar joined: The timestamp when the user joined the club.
    :ivar last_activity_datetime: The last activity as a datetime object.
    :ivar joined_datetime: The joined timestamp as a datetime object.
    """

    id: Optional[str]
    name: Optional[str]
    last_activity: Optional[int]
    icon: Optional[str]
    url: Optional[str]
    joined: Optional[int]

    def __post_init__(self):
        self.last_activity_datetime = from_timestamp(self.last_activity)
        self.joined_datetime = from_timestamp(self.joined)
