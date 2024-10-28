"""
Array of Daily Chess games that a player is currently playing.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-games-current
"""


from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder
from ..utils import from_timestamp


@Client.endpoint
def get_player_current_games(
    username: str, tts=0, **request_options
) -> "GetPlayerCurrentGamesResponse":
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetPlayerCurrentGamesResponse` object containing a list of Daily Chess games
                that a player is currently playing.
    """
    return Resource(
        uri=f"/player/{username}/games",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(ResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetPlayerCurrentGamesResponse(
            json=data,
            text=text,
            games=self._build_games(data.get("games", [])),
        )

    def _build_games(self, data):
        return [
            Game(
                url=game.get("url"),
                move_by=game.get("move_by"),
                pgn=game.get("pgn"),
                time_control=game.get("time_control"),
                start_time=game.get("start_time"),
                last_activity=game.get("last_activity"),
                rated=game.get("rated"),
                turn=game.get("turn"),
                fen=game.get("fen"),
                time_class=game.get("time_class"),
                rules=game.get("rules"),
                white=game.get("white"),
                black=game.get("black"),
                draw_offer=game.get("draw_offer"),
            )
            for game in data
        ]


class GetPlayerCurrentGamesResponse(ChessDotComResponse):
    """
    :ivar games: Array of :obj:`Game`` objects.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json: dict, text: str, games: list) -> None:
        self.games = games
        self.json = json
        self.text = text


@dataclass(repr=True)
class Game(object):
    """
    :ivar url: The URL of the game.
    :ivar move_by: The timestamp by which the next move must be made.
    :ivar pgn: The PGN (Portable Game Notation) of the game.
    :ivar time_control: The time control setting of the game.
    :ivar start_time: The start time of the game as a timestamp.
    :ivar last_activity: The timestamp of the last activity in the game.
    :ivar rated: Indicates if the game is rated.
    :ivar turn: The player whose turn it is to move.
    :ivar fen: The FEN (Forsyth-Edwards Notation) of the current game state.
    :ivar time_class: The time class of the game (e.g., blitz, bullet).
    :ivar rules: The ruleset being used for the game.
    :ivar white: The username of the player with the white pieces.
    :ivar black: The username of the player with the black pieces.
    :ivar draw_offer: Player who has made a draw offer
    """

    url: Optional[str]
    move_by: Optional[int]
    pgn: Optional[str]
    time_control: Optional[str]
    start_time: Optional[int]
    last_activity: Optional[int]
    rated: Optional[bool]
    turn: Optional[str]
    fen: Optional[str]
    time_class: Optional[str]
    rules: Optional[str]
    white: Optional[str]
    black: Optional[str]
    draw_offer: Optional[str]

    def __post_init__(self):
        self.start_datetime = from_timestamp(self.start_time)
        self.last_activity_datetime = from_timestamp(self.last_activity)
