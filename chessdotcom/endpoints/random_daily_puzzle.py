"""
Information about a randomly picked daily puzzle.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-random-daily-puzzle
"""

from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse
from ..utils import from_timestamp


@Client.endpoint
def get_random_daily_puzzle(tts=0, **request_options) -> "GetRandomDailyPuzzleResponse":
    """
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetRandomDailyPuzzleResponse` object containing
                information about a randomly picked daily puzzle.
    """
    return Resource(
        uri="/puzzle/random",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetRandomDailyPuzzleResponse(
            json={"puzzle": data},
            text=text,
            puzzle=Puzzle(
                title=data.get("title"),
                url=data.get("url"),
                publish_time=data.get("publish_time"),
                fen=data.get("fen"),
                pgn=data.get("pgn"),
                image=data.get("image"),
            ),
        )


class GetRandomDailyPuzzleResponse(ChessDotComResponse):
    """
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    :ivar puzzle: Holds the :obj:`Puzzle` object.
    """

    def __init__(self, json, text, puzzle):
        super().__init__(json=json, text=text)
        self.puzzle = puzzle


@dataclass(repr=True)
class Puzzle(object):
    """
    :ivar title: Title of the puzzle.
    :ivar url: URL for the puzzle.
    :ivar publish_time: Time the puzzle was published.
    :ivar fen: FEN string of the puzzle.
    :ivar pgn: PGN string of the puzzle.
    :ivar image: URL for the puzzle image.
    :ivar publish_datetime: Date and time the puzzle was published.
    """

    title: Optional[str]
    url: Optional[str]
    publish_time: Optional[int]
    fen: Optional[str]
    pgn: Optional[str]
    image: Optional[str]

    def __post_init__(self):
        self.publish_datetime = from_timestamp(self.publish_time)
