"""
Daily Chess games where it is the player's turn to act.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-games-tomove
"""


from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse
from ..utils import from_timestamp


@Client.endpoint
def get_player_current_games_to_move(
    username: str, tts=0, **request_options
) -> "GetPlayerCurrentGamesToMoveResponse":
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetPlayerCurrentGamesToMoveResponse` object containing a list of
                Daily Chess games where it is the player's turn to act.
    """
    return Resource(
        uri=f"/player/{username}/games/to-move",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetPlayerCurrentGamesToMoveResponse(
            json=data,
            text=text,
            games=[
                Game(
                    url=game.get("url"),
                    move_by=game.get("move_by"),
                    last_activity=game.get("last_activity"),
                    draw_offer=game.get("draw_offer"),
                )
                for game in data.get("games", [])
            ],
        )


class GetPlayerCurrentGamesToMoveResponse(ChessDotComResponse):
    """
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    :ivar games: List of :obj:`Game` objects.
    """

    def __init__(self, json, text, games):
        super().__init__(json=json, text=text)
        self.games = games


@dataclass(repr=True)
class Game(object):
    """
    :ivar url: URL for the game.
    :ivar move_by: Time when the player must make a move.
    :ivar last_activity: Time of the last activity in the game.
    :ivar draw_offer: True if the player has offered a draw.
    :ivar move_by_datetime: Time when the player must make a move as a datetime object.
    :ivar last_activity_datetime: Time of the last activity in the game as a datetime object.
    """

    url: Optional[str]
    move_by: Optional[int]
    last_activity: Optional[int]
    draw_offer: Optional[bool]

    def __post_init__(self):
        self.move_by_datetime = from_timestamp(self.move_by)
        self.last_activity_datetime = from_timestamp(self.last_activity)
