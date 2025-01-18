"""
List of Team matches the player has attended, is partecipating or is currently

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-player-matches
"""


from dataclasses import dataclass
from typing import List, Optional

from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse
from ..utils import dig


@Client.endpoint
def get_player_team_matches(
    username: str, tts=0, **request_options
) -> "GetPlayerTeamMatchesResponse":
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetPlayerTeamMatchesResponse` object containing a list of team matches
                the player has attended,
                is participating or is currently registered.
    """
    return Resource(
        uri=f"/player/{username}/matches",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetPlayerTeamMatchesResponse(
            json={"matches": data},
            text=text,
            matches=TeamMatches(
                finished=[
                    FinishedMatches(
                        name=match.get("name"),
                        url=match.get("url"),
                        id=match.get("@id"),
                        club=match.get("club"),
                        results=Results(
                            played_as_white=dig(match, ("results", "played_as_white")),
                            played_as_black=dig(match, ("results", "played_as_black")),
                        )
                        if match.get("results")
                        else None,
                        board=match.get("board"),
                    )
                    for match in data.get("finished", [])
                ],
                in_progress=[
                    InProgressMatches(
                        name=match.get("name"),
                        url=match.get("url"),
                        id=match.get("@id"),
                        club=match.get("club"),
                        board=match.get("board"),
                    )
                    for match in data.get("in_progress", [])
                ],
                registered=[
                    RegisteredMatches(
                        name=match.get("name"),
                        url=match.get("url"),
                        id=match.get("@id"),
                        club=match.get("club"),
                    )
                    for match in data.get("registered", [])
                ],
            ),
        )


class GetPlayerTeamMatchesResponse(ChessDotComResponse):
    """
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    :ivar matches: List of :obj:`TeamMatch` objects.
    """

    def __init__(self, json, text, matches):
        super().__init__(json=json, text=text)
        self.matches = matches


@dataclass(repr=True)
class TeamMatches(object):
    """
    :ivar finished: List of :obj:`FinishedMatches` objects.
    :ivar in_progress: List of :obj:`InProgressMatches` objects.
    :ivar registered: List of :obj:`RegisteredMatches` objects.
    """

    finished: List["FinishedMatches"]
    in_progress: List["InProgressMatches"]
    registered: List["RegisteredMatches"]


@dataclass(repr=True)
class FinishedMatches(object):
    """
    :ivar name: The name of the match.
    :ivar url: URL for the match.
    :ivar id: The unique identifier of the match.
    :ivar club: The club of the match.
    :ivar results: The results of the match.
    :ivar board: The board of the match.
    """

    name: Optional[str]
    url: Optional[str]
    id: Optional[int]
    club: Optional[str]
    results: Optional["Results"]
    board: Optional[str]


@dataclass(repr=True)
class InProgressMatches(object):
    """
    :ivar name: The name of the match.
    :ivar url: URL for the match.
    :ivar id: The unique identifier of the match.
    :ivar club: The club of the match.
    :ivar board: The board of the match.
    """

    name: Optional[str]
    url: Optional[str]
    id: Optional[int]
    club: Optional[str]
    board: Optional[str]


@dataclass(repr=True)
class RegisteredMatches(object):
    """
    :ivar name: The name of the match.
    :ivar url: URL for the match.
    :ivar id: The unique identifier of the match.
    :ivar club: The club of the match.
    """

    name: Optional[str]
    url: Optional[str]
    id: Optional[int]
    club: Optional[str]


@dataclass(repr=True)
class Results(object):
    """
    :ivar played_as_white: The result of the player when played as white.
    :ivar played_as_black: The result of the player when played as black.
    """

    played_as_white: Optional[str]
    played_as_black: Optional[str]
