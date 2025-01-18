"""

"""


from dataclasses import dataclass
from typing import List, Optional

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder


@Client.endpoint
def get_leaderboards(tts=0, **request_options) -> ChessDotComResponse:
    """
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`ChessDotComResponse` object containing
                information about top 50 player for daily and live games, tactics and lessons.
    """
    return Resource(
        uri="/leaderboards",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(ResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetLeaderboardsResponse(
            json={"leaderboards": data},
            text=text,
            leaderboards=Leaderboards(
                daily=self._build_leaderboard(data.get("daily")),
                daily960=self._build_leaderboard(data.get("daily960")),
                live_rapid=self._build_leaderboard(data.get("live_rapid")),
                live_bullet=self._build_leaderboard(data.get("live_bullet")),
                live_bughouse=self._build_leaderboard(data.get("live_bughouse")),
                live_blitz=self._build_leaderboard(data.get("live_blitz")),
                live_threecheck=self._build_leaderboard(data.get("live_threecheck")),
                live_crazyhouse=self._build_leaderboard(data.get("live_crazyhouse")),
                live_kingofthehill=self._build_leaderboard(
                    data.get("live_kingofthehill")
                ),
                live_tactics=self._build_leaderboard(data.get("live_tactics")),
                live_rush=self._build_leaderboard(data.get("live_rush")),
                live_battle=self._build_leaderboard(data.get("live_battle")),
                rush=self._build_leaderboard(data.get("rush")),
                tactics=self._build_leaderboard(data.get("tactics")),
                live_blitz960=self._build_leaderboard(data.get("live_blitz960")),
                battle=self._build_leaderboard(data.get("battle")),
            ),
        )

    def _build_leaderboard(self, data):
        return [
            Leaderboard(
                player_id=player.get("player_id"),
                id=player.get("@id"),
                url=player.get("url"),
                username=player.get("username"),
                score=player.get("score"),
                rank=player.get("rank"),
                country=player.get("country"),
                title=player.get("title"),
                name=player.get("name"),
                status=player.get("status"),
                avatar=player.get("avatar"),
                flair_code=player.get("flair_code"),
                win_count=player.get("win_count"),
                loss_count=player.get("loss_count"),
                draw_count=player.get("draw_count"),
                trend_score=self._build_trend_score(player.get("trend_score", {})),
                trend_rank=self._build_trend_rank(player.get("trend_rank", {})),
            )
            for player in data or []
        ]

    def _build_trend_score(self, data):
        return TrendScore(direction=data.get("direction"), delta=data.get("delta"))

    def _build_trend_rank(self, data):
        return TrendRank(direction=data.get("direction"), delta=data.get("delta"))


class GetLeaderboardsResponse(ChessDotComResponse):
    """
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    :ivar leaderboards: Holds the :obj:`Leaderboards` object.
    """

    def __init__(self, json, text, leaderboards):
        self.json = json
        self.text = text
        self.leaderboards = leaderboards


@dataclass(repr=True)
class Leaderboards(object):
    daily: List["Leaderboard"]
    daily960: List["Leaderboard"]
    live_rapid: List["Leaderboard"]
    live_blitz: List["Leaderboard"]
    live_bullet: List["Leaderboard"]
    live_bughouse: List["Leaderboard"]
    live_blitz: List["Leaderboard"]
    live_threecheck: List["Leaderboard"]
    live_crazyhouse: List["Leaderboard"]
    live_kingofthehill: List["Leaderboard"]
    live_tactics: List["Leaderboard"]
    live_rush: List["Leaderboard"]
    live_battle: List["Leaderboard"]
    rush: List["Leaderboard"]
    tactics: List["Leaderboard"]
    live_blitz960: List["Leaderboard"]
    battle: List["Leaderboard"]


@dataclass(repr=True)
class Leaderboard(object):
    player_id: Optional[int]
    id: Optional[str]
    url: Optional[str]
    username: Optional[str]
    score: Optional[int]
    rank: Optional[int]
    country: Optional[str]
    title: Optional[str]
    name: Optional[str]
    status: Optional[str]
    avatar: Optional[str]
    flair_code: Optional[str]
    win_count: Optional[int]
    loss_count: Optional[int]
    draw_count: Optional[int]
    trend_score: Optional["TrendScore"]
    trend_rank: Optional["TrendRank"]


@dataclass(repr=True)
class TrendScore(object):
    direction: Optional[int]
    delta: Optional[int]


@dataclass(repr=True)
class TrendRank(object):
    direction: Optional[int]
    delta: Optional[int]
