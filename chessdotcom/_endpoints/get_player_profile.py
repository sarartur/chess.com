import json

from ..client import Client, Resource
from ..errors import ChessDotComDecodingError
from ..response_builder import ChessDotComResponse, ResponseBuilder


@Client.endpoint
def get_player_profile(username: str, tts=0, **request_options) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing information about
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
            player=Player(
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
                streaming_platforms=data.get("streaming_platforms"),
            ),
        )


class GetPlayerProfileResponse(ChessDotComResponse):
    def __init__(self, json, text, player):
        self.player = player
        self.json = json
        self.text = text


class Player(object):
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
        self.streaming_platforms = streaming_platforms or []
