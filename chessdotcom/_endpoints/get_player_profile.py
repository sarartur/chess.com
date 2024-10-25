import json

from ..client import Client, Resource
from ..errors import ChessDotComDecodingError
from ..response_builder import ChessDotComResponse, ResponseBuilder
from ..utils import from_timestamp


@Client.endpoint
def get_player_profile(username: str, tts=0, **request_options) -> ChessDotComResponse:
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
    def __init__(self, json, text, player):
        self.player = player
        self.json = json
        self.text = text


class PlayerProfile(object):
    def __init__(
        self,
        avatar=None,
        player_id=None,
        id=None,
        url=None,
        name=None,
        username=None,
        title=None,
        followers=None,
        country=None,
        last_online=None,
        joined=None,
        status=None,
        is_streamer=None,
        verified=None,
        league=None,
        location=None,
        streaming_platforms=None,
    ) -> None:
        self.avatar = avatar
        self.player_id = player_id
        self.id = id
        self.url = url
        self.name = name
        self.username = username
        self.title = title
        self.followers = followers
        self.country = country
        self.last_online = last_online
        self.joined = joined
        self.status = status
        self.is_streamer = is_streamer
        self.verified = verified
        self.league = league
        self.location = location
        self.streaming_platforms = streaming_platforms or []

        self.last_online_datetime = from_timestamp(last_online)
        self.joined_datetime = from_timestamp(joined)


class StreamingPlatform(object):
    def __init__(self, type, channel_url) -> None:
        self.type = type
        self.channel_url = channel_url
