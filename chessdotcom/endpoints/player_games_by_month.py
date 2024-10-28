from datetime import datetime
from typing import Optional, Union

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse
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
    )
