"""
List of tournaments the player is registered, is attending or has attended in the past.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-player-tournaments
"""

from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse


@Client.endpoint
def get_player_tournaments(
    username: str, tts=0, **request_options
) -> "GetPlayerTournamentsResponse":
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetPlayerTournamentsResponse` object containing a
                list of tournaments the player is registered,
                is attending or has attended in the past.
    """
    return Resource(
        uri=f"/player/{username}/tournaments",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetPlayerTournamentsResponse(
            json={"tournaments": data},
            text=text,
            tournaments=Tournaments(
                finished=[
                    FinishedTournament(
                        url=tournament.get("url"),
                        id=tournament.get("@id"),
                        wins=tournament.get("wins"),
                        losses=tournament.get("losses"),
                        draws=tournament.get("draws"),
                        placement=tournament.get("placement"),
                        status=tournament.get("status"),
                        total_players=tournament.get("total_players"),
                        time_class=tournament.get("time_class"),
                        type=tournament.get("type"),
                    )
                    for tournament in data.get("finished", [])
                ],
                in_progress=[
                    InProgressTournament(
                        url=tournament.get("url"),
                        id=tournament.get("@id"),
                        status=tournament.get("status"),
                    )
                    for tournament in data.get("in_progress", [])
                ],
                registered=[
                    RegisteredTournament(
                        url=tournament.get("url"),
                        id=tournament.get("@id"),
                        status=tournament.get("status"),
                    )
                    for tournament in data.get("registered", [])
                ],
            ),
        )


class GetPlayerTournamentsResponse(ChessDotComResponse):
    """
    :ivar json: The JSON response from the API.
    :ivar text: The text response from the API.
    :ivar tournaments: :obj:`Tournaments`: contains finished,
                        in-progress, and registered tournaments.
    """

    def __init__(self, json, text, tournaments):
        super().__init__(json=json, text=text)
        self.tournaments = tournaments


@dataclass(repr=True)
class Tournaments(object):
    """
    :ivar finished: List of :obj:`FinishedTournament` objects.
    :ivar in_progress: List of :obj:`InProgressTournament` objects.
    :ivar registered: List of :obj:`RegisteredTournament` objects.
    """

    finished: list
    in_progress: list
    registered: list


@dataclass(repr=True)
class FinishedTournament(object):
    """
    Represents a finished tournament.

    :ivar url: The URL of the tournament.
    :ivar id: The unique identifier of the tournament.
    :ivar wins: The number of wins by the player in the tournament.
    :ivar losses: The number of losses by the player in the tournament.
    :ivar draws: The number of draws by the player in the tournament.
    :ivar placement: The final placement of the player in the tournament.
    :ivar status: The status of the tournament.
    :ivar total_players: The total number of players in the tournament.
    :ivar time_class: The time control class of the tournament (e.g., blitz, bullet, rapid).
    :ivar type: The type of the tournament.
    """

    url: Optional[str]
    id: Optional[str]
    wins: Optional[int]
    losses: Optional[int]
    draws: Optional[int]
    placement: Optional[int]
    status: Optional[str]
    total_players: Optional[int]
    time_class: Optional[str]
    type: Optional[str]


@dataclass(repr=True)
class InProgressTournament(object):
    """
    Represents an in-progress tournament.

    :ivar url: The URL of the tournament.
    :ivar id: The unique identifier of the tournament.
    :ivar status: The current status of the tournament.
    """

    url: Optional[str]
    id: Optional[str]
    status: Optional[str]


@dataclass(repr=True)
class RegisteredTournament(object):
    """
    Represents a registered tournament.

    :ivar url: The URL of the tournament.
    :ivar id: The unique identifier of the tournament.
    :ivar status: The current status of the tournament.
    """

    url: Optional[str]
    id: Optional[str]
    status: Optional[str]
