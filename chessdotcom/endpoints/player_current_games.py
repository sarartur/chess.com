from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder


@Client.endpoint
def get_player_current_games(
    username: str, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of Daily Chess games
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
            )
            for game in data
        ]


class GetPlayerCurrentGamesResponse(ChessDotComResponse):
    """
    :ivar games: array of URLs for monthly archives in ascending chronological order.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json: dict, text: str, games: list) -> None:
        self.games = games
        self.json = json
        self.text = text


@dataclass(repr=True)
class Game(object):
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
