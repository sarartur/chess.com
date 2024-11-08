"""
List of tournaments the player is registered, is attending or has attended in the past.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-player-tournaments
"""

from dataclasses import dataclass

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder


@Client.endpoint
def get_player_tournaments(
    username: str, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a
                list of tournaments the player is registered,
                is attending or has attended in the past.
    """
    return Resource(
        uri=f"/player/{username}/tournaments",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(ResponseBuilder):
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
                        id=tournament.get("id"),
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
        self.json = json
        self.text = text
        self.tournaments = tournaments


@dataclass(repr=True)
class Tournaments(object):
    finished: list
    in_progress: list
    registered: list


@dataclass(repr=True)
class FinishedTournament(object):
    url: str
    id: str
    wins: int
    losses: int
    draws: int
    placement: int
    status: str
    total_players: int
    time_class: str
    type: str


@dataclass(repr=True)
class InProgressTournament(object):
    url: str
    id: str
    status: str


@dataclass(repr=True)
class RegisteredTournament(object):
    url: str
    id: str
    status: str
