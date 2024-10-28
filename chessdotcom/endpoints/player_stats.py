"""
Ratings, win/loss, and other stats about a player's game play,
tactics, lessons and Puzzle Rush score.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-player-stats
"""

from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder
from ..utils import dig, from_timestamp


@Client.endpoint
def get_player_stats(
    username: str, tts=0, **request_options
) -> "GetPlayerStatsResponse":
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetPlayerStatsResponse`: information about the
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
                chess_daily=self._build_game_stats(data.get("chess_daily")),
                chess960_daily=self._build_game_stats(data.get("chess960_daily")),
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
            tournament=TournamentGameStats(
                count=dig(data, ("tournament", "count")),
                withdraw=dig(data, ("tournament", "withdraw")),
                points=dig(data, ("tournament", "points")),
                highest_finish=dig(data, ("tournament", "highest_finish")),
            )
            if data.get("tournament")
            else None,
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
    """
    :ivar fide: The FIDE rating of the player.
    :ivar chess_daily: :obj:`GameStats`: the player's statistics in daily chess games.
    :ivar chess960_daily: :obj:`GameStats`: the player's statistics in daily chess960 games.
    :ivar chess_rapid: :obj:`GameStats`: the player's statistics in rapid chess games.
    :ivar chess_bullet: :obj:`GameStats`: the player's statistics in bullet chess games.
    :ivar chess_blitz: :obj:`GameStats`: the player's statistics in blitz chess games.
    :ivar tactics: :obj:`TacticStats`: the player's statistics in chess tactics.
    :ivar puzzle_rush: :obj:`PuzzleRushStats`: the player's statistics in puzzle rush challenges.
    """

    fide: Optional[int]
    chess_daily: Optional["GameStats"]
    chess960_daily: Optional["GameStats"]
    chess_rapid: Optional["GameStats"]
    chess_bullet: Optional["GameStats"]
    chess_blitz: Optional["GameStats"]
    tactics: Optional["TacticStats"]
    puzzle_rush: Optional["PuzzleRushStats"]


@dataclass(repr=True)
class GameStats(object):
    """
    :ivar last: :obj:`LastGameStats`: the player's last game statistics.
    :ivar best: :obj:`BestGameStats`: the player's best game statistics.
    :ivar record: :obj:`RecordGameStats`: the player's record game statistics.
    :ivar tournament: :obj:`TournamentGameStats`: the player's tournament game statistics
    """

    last: "LastGameStats"
    best: "BestGameStats"
    record: "RecordGameStats"
    tournament: Optional["TournamentGameStats"]


@dataclass(repr=True)
class LastGameStats(object):
    """
    :ivar rating: The rating of the last game.
    :ivar date: The date of the last game.
    :ivar rd: The rating deviation of the last game.
    :ivar datetime: The datetime representation of the date.
    """

    rating: Optional[int]
    date: Optional[int]
    rd: Optional[int]

    def __post_init__(self):
        self.datetime = from_timestamp(self.date)


@dataclass(repr=True)
class BestGameStats(object):
    """
    :ivar rating: The rating of the best game.
    :ivar date: The date of the best game.
    :ivar game: The URL or identifier of the best game.
    :ivar datetime: The datetime representation of the date.
    """

    rating: Optional[int]
    date: Optional[int]
    game: Optional[str]

    def __post_init__(self):
        self.datetime = from_timestamp(self.date)


@dataclass(repr=True)
class RecordGameStats(object):
    """
    :ivar win: Number of wins.
    :ivar loss: Number of losses.
    :ivar draw: Number of draws.
    """

    win: Optional[int]
    loss: Optional[int]
    draw: Optional[int]


@dataclass(repr=True)
class TournamentGameStats(object):
    """
    :ivar count: The number of tournament games played.
    :ivar withdraw: The number of tournaments withdrawn from.
    :ivar points: The total points accumulated in tournaments.
    :ivar highest_finish: The highest finish position in a tournament.
    """

    count: Optional[int]
    withdraw: Optional[int]
    points: Optional[float]
    highest_finish: Optional[int]


@dataclass(repr=True)
class TacticStats(object):
    """
    :ivar highest: :obj:`TacticStatsRecord`: the highest tactic stats record.
    :ivar lowest: :obj:`TacticStatsRecord`: the lowest tactic stats record.
    """

    highest: "TacticStatsRecord"
    lowest: "TacticStatsRecord"


@dataclass(repr=True)
class TacticStatsRecord(object):
    """
    :ivar rating: The rating of the tactic stats record.
    :ivar date: The date of the tactic stats record.
    :ivar datetime: The datetime representation of the the date.
    """

    rating: Optional[int]
    date: Optional[int]

    def __post_init__(self):
        self.datetime = from_timestamp(self.date)


@dataclass(repr=True)
class PuzzleRushStats(object):
    """
    :ivar best: :obj:`PuzzleRushRecord`: the best puzzle rush stats.
    """

    best: "PuzzleRushRecord"


@dataclass(repr=True)
class PuzzleRushRecord(object):
    """
    :ivar total_attempts: The total number of attempts made in the puzzle rush.
    :ivar score: The score achieved in the puzzle rush.
    """

    total_attempts: Optional[int]
    score: Optional[int]
