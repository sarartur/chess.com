"""
Get details about a tournament's round.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-tournament-round
"""

from dataclasses import dataclass
from typing import List, Optional

from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse


@Client.endpoint
def get_tournament_round(
    url_id: str, round_num: int, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param round_num: the round of the tournament.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetTournamentRoundResponse` object containing
                 details about a tournament's round.
    """
    return Resource(
        uri=f"/tournament/{url_id}/{round_num}",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetTournamentRoundResponse(
            json={"tournament_round": data},
            text=text,
            tournament_round=TournamentRound(
                groups=data.get("groups", []),
                players=[
                    TournamentPlayer(
                        username=player.get("username"),
                        is_advancing=player.get("is_advancing"),
                    )
                    for player in data.get("players", [])
                ],
            ),
        )


class GetTournamentRoundResponse(ChessDotComResponse):
    """
    :ivar tournament_round: Holds the :obj:`TournamentRound` object.
    :ivar json: The JSON response from the API.
    :ivar text: The raw response from the API.
    """

    def __init__(self, tournament_round, json, text):
        self.tournament_round = tournament_round
        super().__init__(json=json, text=text)


@dataclass(repr=True)
class TournamentRound(object):
    """
    :ivar players: list of players in the round. Holds :obj:`TournamentPlayer` objects.
    :ivar groups: list of groups in the round.
    """

    groups: List[str]
    players: List["TournamentPlayer"]


@dataclass(repr=True)
class TournamentPlayer(object):
    """
    :ivar username: username of the player.
    :ivar is_advancing: whether the player is advancing to the next round.
    """

    username: Optional[str]
    is_advancing: Optional[bool]
