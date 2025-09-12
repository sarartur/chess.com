"""
Complete Live Archive by Time Control

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-games-archive-live
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union

from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse
from ..utils import from_timestamp


@Client.endpoint
def get_player_games_by_basetime_increment(
    username: str,
    basetime: Union[str, int],
    increment: Optional[Union[str, int, None]] = None,
    tts=0,
    **request_options,
) -> "GetPlayerGamesByBasetimeIncrementResponse":
    """
    :param username: username of the player.
    :param basetime: the base time control in seconds.
    :param increment: the increment in seconds (optional).
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetPlayerGamesByBasetimeIncrementResponse` object containing a list of live
                Chess games that a player has finished by time control.
    """
    if increment is not None:
        uri = f"/player/{username}/games/live/{basetime}/{increment}"
    else:
        uri = f"/player/{username}/games/live/{basetime}"
    
    return Resource(
        uri=uri,
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetPlayerGamesByBasetimeIncrementResponse(
            json=data,
            text=text,
            games=self._build_games(data.get("games", [])),
        )

    def _build_games(self, data):
        return [
            Game(
                url=game.get("url"),
                pgn=game.get("pgn"),
                time_control=game.get("time_control"),
                end_time=game.get("end_time"),
                rated=game.get("rated"),
                accuracies=self._build_accuracies(game.get("accuracies")),
                fen=game.get("fen"),
                time_class=game.get("time_class"),
                rules=game.get("rules"),
                eco=game.get("eco"),
                white=self._build_player_stats(game.get("white")),
                black=self._build_player_stats(game.get("black")),
            )
            for game in data
        ]

    def _build_accuracies(self, data):
        if not data:
            return

        return Accuracies(white=data.get("white"), black=data.get("black"))

    def _build_player_stats(self, data):
        if not data:
            return

        return PlayerStats(
            rating=data.get("rating"),
            result=data.get("result"),
            username=data.get("username"),
            id=data.get("@id"),
            uuid=data.get("uuid"),
        )


class GetPlayerGamesByBasetimeIncrementResponse(ChessDotComResponse):
    """
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    :ivar games: A list of :obj:`LiveGame` objects.
    """

    def __init__(self, json, text, games):
        super().__init__(json=json, text=text)
        self.games = games


@dataclass(repr=True)
class Game(object):
    """
    :ivar url: URL of the game.
    :ivar pgn: PGN (Portable Game Notation) of the game.
    :ivar time_control: Time control of the game.
    :ivar end_time: End time of the game in epoch format.
    :ivar rated: Whether the game was rated.
    :ivar accuracies: :obj:`LiveGameAccuracies`: accuracies of the players in the game.
    :ivar fen: FEN (Forsyth-Edwards Notation) of the game.
    :ivar time_class: Time class of the game.
    :ivar rules: Rules of the game.
    :ivar eco: ECO (Encyclopaedia of Chess Openings) URL of the game.
    :ivar white: :obj:`LivePlayerStats`: stats of the white player.
    :ivar black: :obj:`LivePlayerStats`: stats of the black player.
    """

    url: Optional[str]
    pgn: Optional[str]
    time_control: Optional[str]
    end_time: Optional[int]
    rated: Optional[bool]
    accuracies: Optional["Accuracies"]
    fen: Optional[str]
    time_class: Optional[str]
    rules: Optional[str]
    eco: Optional[str]
    white: Optional["PlayerStats"]
    black: Optional["PlayerStats"]

    def __post_init__(self):
        self.end_datetime = from_timestamp(self.end_time)


@dataclass(repr=True)
class Accuracies(object):
    """
    :ivar white: Accuracy score for the white player.
    :ivar black: Accuracy score for the black player.
    """

    white: Optional[float]
    black: Optional[float]


@dataclass(repr=True)
class PlayerStats(object):
    """
    :ivar rating: The player's rating.
    :ivar result: The result of the game for the player.
    :ivar username: The username of the player.
    :ivar id: The ID of the player.
    :ivar uuid: The UUID of the player.
    """

    rating: Optional[int]
    result: Optional[str]
    username: Optional[str]
    id: Optional[str]
    uuid: Optional[str]