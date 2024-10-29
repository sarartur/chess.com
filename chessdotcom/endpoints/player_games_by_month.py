"""
List of Live and Daily Chess games that a player has finished.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-games-archive
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder
from ..utils import resolve_date


@Client.endpoint
def get_player_games_by_month(
    username: str,
    year: Optional[Union[str, int, None]] = None,
    month: Optional[Union[str, int, None]] = None,
    datetime_obj: Optional[Union[datetime, None]] = None,
    tts=0,
    **request_options,
) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param year: the year (yyyy).
    :param month: the month (mm).
    :param date: datetime.datetime of the month. Can be passed in instead of month
                    and year parameters.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of live and daily
                Chess games that a player has finished.
    """
    yyyy, mm = resolve_date(year, month, datetime_obj)
    return Resource(
        uri=f"/player/{username}/games/{yyyy}/{mm}",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(ResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetPlayerGamesByMonthResponse(
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
                start_time=game.get("start_time"),
                end_time=game.get("end_time"),
                accuracies=self._build_accuracies(game.get("accuracies")),
                tcn=game.get("tcn"),
                uuid=game.get("uuid"),
                initial_setup=game.get("initial_setup"),
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


class GetPlayerGamesByMonthResponse(ChessDotComResponse):
    def __init__(self, json, text, games):
        self.text = text
        self.json = json
        self.games = games


@dataclass(repr=True)
class Game(object):
    url: Optional[str]
    pgn: Optional[str]
    time_control: Optional[str]
    start_time: Optional[int]
    end_time: Optional[int]
    accuracies: Optional["Accuracies"]
    tcn: Optional[str]
    uuid: Optional[str]
    initial_setup: Optional[str]
    fen: Optional[str]
    time_class: Optional[str]
    rules: Optional[str]
    eco: Optional[str]
    white: Optional["PlayerStats"]
    black: Optional["PlayerStats"]


@dataclass(repr=True)
class Accuracies(object):
    white: Optional[str]
    black: Optional[str]


@dataclass(repr=True)
class PlayerStats(object):
    rating: Optional[int]
    result: Optional[str]
    username: Optional[str]
    id: Optional[str]
    uuid: Optional[str]
