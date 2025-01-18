"""
Get details about a team match and players playing that match.
After the match is finished there will be a link to each player's stats endpoint,
in order to get up-to-date information about the player.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-match-live-profile
"""

from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse
from ..utils import dig, from_timestamp


@Client.endpoint
def get_team_match_live(
    match_id: int, tts=0, **request_options
) -> "GetTeamMatchLiveResponse":
    """
    :param match_id: the id of the match.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetTeamMatchLiveResponse` object containing
                details about a team match and players playing that match.
    """
    return Resource(
        uri=f"/match/live/{match_id}",
        tts=tts,
        response_builder=ResponseBuilder(),
        request_options=request_options,
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetTeamMatchLiveResponse(
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
                    time_increment=dig(data, ("settings", "time_increment")),
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
            fair_play_removals=data.get("fair_play_removals", []),
        )

    def _build_player(self, data):
        return Player(
            username=data.get("username"),
            board=data.get("board"),
            stats=data.get("stats"),
            status=data.get("status"),
            played_as_black=data.get("played_as_black"),
            played_as_white=data.get("played_as_white"),
            rating=data.get("rating"),
            timeout_percent=data.get("timeout_percent"),
        )


class GetTeamMatchLiveResponse(ChessDotComResponse):
    """
    :ivar match: Holds the :obj:`TeamMatch` object.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json, text, match):
        super().__init__(json=json, text=text)
        self.match = match


@dataclass(repr=True)
class TeamMatch(object):
    """
    :ivar name: The name of the match.
    :ivar url: The URL of the match.
    :ivar id: The unique identifier of the match.
    :ivar status: The current status of the match.
    :ivar start_time: The start time of the match in Unix timestamp.
    :ivar end_time: The end time of the match in Unix timestamp.
    :ivar boards: The number of boards in the match.
    :ivar settings: The settings of the team match. Holds the :obj:`TeamMatchSettings` object.
    :ivar teams: The teams participating in the match. Holds the :obj:`Teams` object.
    :ivar start_datetime: The start time of the match as a datetime object.
    :ivar end_datetime: The end time of the match as a datetime object.
    """

    name: Optional[str]
    url: Optional[str]
    id: Optional[str]
    status: Optional[str]
    start_time: Optional[int]
    end_time: Optional[int]
    boards: Optional[int]
    settings: "TeamMatchSettings"
    teams: "Teams"

    def __post_init__(self):
        self.start_datetime = from_timestamp(self.start_time)
        self.end_datetime = from_timestamp(self.end_time)


@dataclass(repr=True)
class TeamMatchSettings(object):
    """
    :ivar rules: The rules of the match.
    :ivar time_class: The time class of the match.
    :ivar time_control: The time control of the match.
    :ivar time_increment: The time increment of the match.
    :ivar min_team_players: The minimum number of players required in the team.
    :ivar max_team_players: The maximum number of players required in the team.
    :ivar min_required_games: The minimum number of games required to finish the match.
    :ivar min_rating: The minimum rating required to participate in the match.
    :ivar max_rating: The maximum rating required to participate in the match.
    :ivar autostart: Whether the match will start automatically.
    """

    rules: Optional[str]
    time_class: Optional[str]
    time_control: Optional[str]
    time_increment: Optional[int]
    min_team_players: Optional[int]
    max_team_players: Optional[int]
    min_required_games: Optional[int]
    min_rating: Optional[int]
    max_rating: Optional[int]
    autostart: Optional[bool]


@dataclass(repr=True)
class Teams(object):
    """
    :ivar team1: The first team participating in the match. Holds the :obj:`Team` object.
    :ivar team2: The second team participating in the match. Holds the :obj:`Team` object
    """

    team1: Optional["Team"]
    team2: Optional["Team"]


@dataclass(repr=True)
class Team(object):
    """
    :ivar id: The unique identifier of the team.
    :ivar name: The name of the team.
    :ivar url: The URL of the team.
    :ivar score: The score of the team.
    :ivar result: The result of the team.
    :ivar fair_play_removals: List of usernames of players removed due to fair play violations.
    :ivar players: List of :obj:`Player` objects.
    """

    id: Optional[str]
    name: Optional[str]
    url: Optional[str]
    score: Optional[float]
    result: Optional[str]
    players: list["Player"]
    fair_play_removals: list[str]


@dataclass(repr=True)
class Player(object):
    """
    :ivar username: The username of the player.
    :ivar board: The board the player is playing on.
    :ivar stats: The stats of the player.
    :ivar status: The status of the player.
    :ivar played_as_black: The result {win, lose, resign, etc.} of player when played as black.
    :ivar played_as_white: The result {win, lose, resign, etc.} of player when played as white.
    :ivar rating: The rating of the player.
    :ivar timeout_percent: The timeout percentage of the player

    """

    username: Optional[str]
    board: Optional[str]
    stats: Optional[str]
    status: Optional[str]
    played_as_black: Optional[str]
    played_as_white: Optional[str]
    rating: Optional[int]
    timeout_percent: Optional[float]
