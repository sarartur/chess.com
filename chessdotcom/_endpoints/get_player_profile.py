import json
from dataclasses import dataclass, field
from typing import List, Optional

from ..client import Client, Resource
from ..errors import ChessDotComDecodingError
from ..response_builder import ChessDotComResponse, ResponseBuilder
from ..utils import from_timestamp


@Client.endpoint
def get_player_profile(
    username: str, tts=0, **request_options
) -> "GetPlayerProfileResponse":
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``GetPlayerProfileResponse`` object containing information about
                the player's profile.
    """
    return Resource(
        uri=f"/player/{username}",
        tts=tts,
        top_level_attribute="player",
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(ResponseBuilder):
    def build(self, text):
        try:
            data = json.loads(text)
        except json.JSONDecodeError as err:
            raise ChessDotComDecodingError(
                text, "Response could not be converted to JSON"
            ) from err

        return GetPlayerProfileResponse(
            json=data,
            text=text,
            player=PlayerProfile(
                avatar=data.get("avatar"),
                player_id=data.get("player_id"),
                id=data.get("@id"),
                url=data.get("url"),
                name=data.get("name"),
                username=data.get("username"),
                title=data.get("title"),
                followers=data.get("followers"),
                country=data.get("country"),
                last_online=data.get("last_online"),
                joined=data.get("joined"),
                status=data.get("status"),
                is_streamer=data.get("is_streamer"),
                verified=data.get("verified"),
                league=data.get("league"),
                location=data.get("location"),
                streaming_platforms=self._build_steaming_platforms(
                    data.get("streaming_platforms", [])
                ),
            ),
        )

    def _build_steaming_platforms(self, data):
        return [
            StreamingPlatform(type=d.get("type"), channel_url=d.get("channel_url"))
            for d in data
        ]


class GetPlayerProfileResponse(ChessDotComResponse):
    """
    A response object for the ``get_player_profile`` endpoint.
    :ivar player: The player for whom the profile is retrieved.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json: dict, text: str, player: "PlayerProfile"):
        self.player = player
        self.json = json
        self.text = text


@dataclass(repr=True)
class PlayerProfile:
    avatar: Optional[str]
    player_id: Optional[int]
    id: Optional[str]
    url: Optional[str]
    name: Optional[str]
    username: Optional[str]
    title: Optional[str]
    followers: Optional[int]
    country: Optional[str]
    last_online: Optional[int]
    joined: Optional[int]
    status: Optional[str]
    is_streamer: Optional[bool]
    verified: Optional[bool]
    league: Optional[str]
    location: Optional[str]
    streaming_platforms: List["StreamingPlatform"]
    last_online_datetime: Optional[str] = field(init=False)
    joined_datetime: Optional[str] = field(init=False)

    def __post_init__(self):
        self.last_online_datetime = from_timestamp(self.last_online)
        self.joined_datetime = from_timestamp(self.joined)


@dataclass
class StreamingPlatform:
    type: Optional[str]
    channel_url: Optional[str]
