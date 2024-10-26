from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_player_stats(username: str, tts=0, **request_options) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing information about the
                plyers's ratings, win/loss, and other stats.
    """
    return Resource(
        uri=f"/player/{username}/stats",
        tts=tts,
        top_level_attribute="stats",
        request_options=request_options,
    )


class GetPlayerStatsResponse(ChessDotComResponse):
    """
    :ivar stats: Holds the :obj:`PlayerStats` object.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json: dict, text: str, stats: "PlayerStats"):
        self.stats = stats
        self.json = json
        self.text = text


@dataclass(repr=True)
class PlayerStats(object):
    fide: Optional[int]
    chess_rapid: "GameStats"
    chess_bullet: "GameStats"
    chess_blitz: "GameStats"
    tactics: "TacticStats"
    puzzle_rush: "PuzzleRushStats"


@dataclass(repr=True)
class GameStats(object):
    last: "LastGameStats"
    best: "BestGameStats"
    record: "RecordGameStats"


@dataclass(repr=True)
class LastGameStats(object):
    rating: Optional[int]
    date: Optional[int]
    rd: Optional[int]


@dataclass(repr=True)
class BestGameStats(object):
    rating: Optional[int]
    date: Optional[int]
    game: Optional[str]


@dataclass(repr=True)
class RecordGameStats(object):
    win: Optional[int]
    loss: Optional[int]
    draw: Optional[int]


@dataclass(repr=True)
class TacticStats(object):
    highest: "TacticStatsRecord"
    lowest: "TacticStatsRecord"


@dataclass(repr=True)
class TacticStatsRecord(object):
    rating: Optional[int]
    date: Optional[int]


@dataclass(repr=True)
class PuzzleRushStats(object):
    best: "PuzzleRushRecord"


@dataclass(repr=True)
class PuzzleRushRecord(object):
    total_attempts: Optional[int]
    score: Optional[int]
