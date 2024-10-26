from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder
from ..utils import dig


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
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(ResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetPlayerStatsResponse(
            json={"stats": data},
            text=text,
            stats=PlayerStats(
                fide=data.get("fide"),
                chess_rapid=self._build_game_stats(data.get("chess_rapid")),
                chess_bullet=self._build_game_stats(data.get("chess_bullet")),
                chess_blitz=self._build_game_stats(data.get("chess_blitz")),
                tactics=self._build_tactics_stats(data.get("tactics")),
                puzzle_rush=self._build_puzzle_rush_stats(data.get("puzzle_rush")),
            ),
        )

    def _build_game_stats(self, data):
        if not data:
            return

        return GameStats(
            last=LastGameStats(
                rating=dig(data, ("last", "rating")),
                date=dig(data, ("last", "date")),
                rd=dig(data, ("last", "rd")),
            ),
            best=BestGameStats(
                rating=dig(data, ("best", "rating")),
                date=dig(data, ("best", "date")),
                game=dig(data, ("best", "game")),
            ),
            record=RecordGameStats(
                win=dig(data, ("record", "win")),
                loss=dig(data, ("record", "loss")),
                draw=dig(data, ("record", "draw")),
            ),
        )

    def _build_tactics_stats(self, data):
        if not data:
            return

        return TacticStats(
            highest=TacticStatsRecord(
                rating=dig(data, ("highest", "rating")),
                date=dig(data, ("highest", "date")),
            ),
            lowest=TacticStatsRecord(
                rating=dig(data, ("lowest", "rating")),
                date=dig(data, ("lowest", "date")),
            ),
        )

    def _build_puzzle_rush_stats(self, data):
        if not data:
            return

        return PuzzleRushStats(
            best=PuzzleRushRecord(
                total_attempts=dig(data, ("best", "total_attempts")),
                score=dig(data, ("best", "score")),
            )
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
    chess_rapid: Optional["GameStats"]
    chess_bullet: Optional["GameStats"]
    chess_blitz: Optional["GameStats"]
    tactics: Optional["TacticStats"]
    puzzle_rush: Optional["PuzzleRushStats"]


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
