from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder
from ..utils import dig


@Client.endpoint
def get_team_match(match_id: int, tts=0, **request_options) -> ChessDotComResponse:
    """
    :param match_id: the id of the match.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                details about a team match and players playing that match.
    """
    return Resource(
        uri=f"/match/{match_id}",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(ResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetTeamMatchResponse(
            json={"match": data},
            text=text,
            match=TeamMatch(
                name=data.get("name"),
                url=data.get("url"),
                id=data.get("@id"),
                status=data.get("status"),
                start_time=data.get("start_time"),
                end_time=data.get("end_time"),
                boards=data.get("boards"),
                settings=TeamMatchSettings(
                    rules=dig(data, ("settings", "rules")),
                    time_class=dig(data, ("settings", "time_class")),
                    time_control=dig(data, ("settings", "time_control")),
                    min_team_players=dig(data, ("settings", "min_team_players")),
                    max_team_players=dig(data, ("settings", "max_team_players")),
                    min_required_games=dig(data, ("settings", "min_required_games")),
                    min_rating=dig(data, ("settings", "min_rating")),
                    max_rating=dig(data, ("settings", "max_rating")),
                    autostart=dig(data, ("settings", "autostart")),
                ),
                teams=Teams(
                    team1=self._build_team(dig(data, ("teams", "team1"))),
                    team2=self._build_team(dig(data, ("teams", "team2"))),
                ),
            ),
        )

    def _build_team(self, data):
        if not data:
            return None

        return Team(
            id=data.get("@id"),
            name=data.get("name"),
            url=data.get("url"),
            score=data.get("score"),
            result=data.get("result"),
            players=[self._build_player(d) for d in data.get("players", [])],
        )

    def _build_player(self, data):
        return Player(
            username=data.get("username"),
            board=data.get("board"),
            stats=data.get("stats"),
            status=data.get("status"),
            played_as_black=data.get("played_as_black"),
            rating=data.get("rating"),
            timeout_percent=data.get("timeout_percent"),
        )


class GetTeamMatchResponse(ChessDotComResponse):
    """
    :ivar match: Holds the :obj:`TeamMatch` object.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json, text, match):
        self.json = json
        self.text = text
        self.match = match


@dataclass(repr=True)
class TeamMatch(object):
    name: Optional[str]
    url: Optional[str]
    id: Optional[str]
    status: Optional[str]
    start_time: Optional[int]
    end_time: Optional[int]
    boards: Optional[int]
    settings: "TeamMatchSettings"
    teams: "Teams"


@dataclass(repr=True)
class TeamMatchSettings(object):
    rules: Optional[str]
    time_class: Optional[str]
    time_control: Optional[str]
    min_team_players: Optional[int]
    max_team_players: Optional[int]
    min_required_games: Optional[int]
    min_rating: Optional[int]
    max_rating: Optional[int]
    autostart: Optional[bool]


@dataclass(repr=True)
class Teams(object):
    team1: Optional["Team"]
    team2: Optional["Team"]


@dataclass(repr=True)
class Team(object):
    id: Optional[str]
    name: Optional[str]
    url: Optional[str]
    score: Optional[float]
    result: Optional[str]
    players: list["Player"]


@dataclass(repr=True)
class Player(object):
    username: Optional[str]
    board: Optional[str]
    stats: Optional[str]
    status: Optional[str]
    played_as_black: Optional[str]
    played_as_white: Optional[str]
    rating: Optional[int]
    timeout_percent: Optional[float]
