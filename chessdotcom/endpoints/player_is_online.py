"""
Player online status

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-player-is-online
"""

from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse


@Client.endpoint
def get_player_is_online(
    username: str,
    tts=0,
    **request_options,
) -> "GetPlayerIsOnlineResponse":
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetPlayerIsOnlineResponse` object containing the player's online status.
    """
    return Resource(
        uri=f"/player/{username}/is-online",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetPlayerIsOnlineResponse(
            json=data,
            text=text,
            online=data.get("online"),
        )


class GetPlayerIsOnlineResponse(ChessDotComResponse):
    """
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    :ivar online: Whether the player is online (has been online in the last five minutes).
    """

    def __init__(self, json, text, online):
        super().__init__(json=json, text=text)
        self.online = online


@dataclass(repr=True)
class PlayerOnlineStatus(object):
    """
    :ivar online: True if the player has been online in the last five minutes, False otherwise.
    """

    online: Optional[bool]