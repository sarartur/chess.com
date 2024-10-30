from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder
from ..utils import resolve_date


@Client.endpoint
def get_player_games_by_month_pgn(
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
    :returns: ``ChessDotComResponse`` object containing
                standard multi-game format PGN containing all games for a month.
    """
    yyyy, mm = resolve_date(year, month, datetime_obj)
    return Resource(
        uri=f"/player/{username}/games/{yyyy}/{mm}/pgn",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(ResponseBuilder):
    def build(self, text):
        return GetPlayerGamesByMonthResponsePgn(
            json={"pgn": {"pgn": text, "data": text}},
            text=text,
            pgn=Pgn(pgn=text, data=text),
        )


class GetPlayerGamesByMonthResponsePgn(ChessDotComResponse):
    def __init__(self, json, text, pgn):
        self.json = json
        self.text = text
        self.pgn = pgn


@dataclass(repr=True)
class Pgn(object):
    pgn: Optional[str]
    data: Optional[str]
