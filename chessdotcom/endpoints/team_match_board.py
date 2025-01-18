"""
Get details about a team match board.
Only in-progress or finished games will be included,
so there may be one or two games in this list.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-match-board
"""

from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse
from ..utils import from_timestamp


@Client.endpoint
def get_team_match_board(
    match_id: int, board_num: int, tts=0, **request_options
) -> "GetTeamMatchBoardResponse":
    """
    :param match_id: the id of the match.
    :param board_num: the number of the board.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetTeamMatchBoardResponse` object containing
                details about a team match board.
    """
    return Resource(
        uri=f"/match/{match_id}/{board_num}",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetTeamMatchBoardResponse(
            json={"match_board": data},
            text=text,
            match_board=MatchBoard(
                board_scores=data.get("board_scores"),
                games=[
                    Game(
                        url=game.get("url"),
                        pgn=game.get("pgn"),
                        time_control=game.get("time_control"),
                        end_time=game.get("end_time"),
                        start_time=game.get("start_time"),
                        rated=game.get("rated"),
                        fen=game.get("fen"),
                        time_class=game.get("time_class"),
                        rules=game.get("rules"),
                        match=game.get("match"),
                        white=self._build_player(game.get("white")),
                        black=self._build_player(game.get("black")),
                    )
                    for game in data.get("games", [])
                ],
            ),
        )

    def _build_player(self, data):
        if data is None:
            return

        return GamePlayer(
            rating=data.get("rating"),
            result=data.get("result"),
            id=data.get("@id"),
            username=data.get("username"),
            uuid=data.get("uuid"),
        )


class GetTeamMatchBoardResponse(ChessDotComResponse):
    """
    :ivar match_board: Holds the :obj:`MatchBoard` object.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json, text, match_board):
        super().__init__(json=json, text=text)
        self.match_board = match_board


@dataclass(repr=True)
class MatchBoard(object):
    """
    :ivar board_scores: The board scores as a dictionary.
    :ivar games: List of :obj:`Game` objects.
    """

    games: list["Game"]
    board_scores: Optional[dict]


@dataclass(repr=True)
class Game(object):
    """
    :ivar url: URL for the game.
    :ivar pgn: The PGN of the game.
    :ivar time_control: The time control of the game.
    :ivar end_time: The end time of the game.
    :ivar start_time: The start time of the game.
    :ivar rated: Whether the game is rated.
    :ivar fen: The FEN of the game.
    :ivar time_class: The time class of the game.
    :ivar rules: The rules of the game.
    :ivar match: The match of the game.
    :ivar end_datetime: The end time as a datetime object.
    :ivar start_datetime: The start time as a datetime object.
    :ivar white: The white player of the game. Holds the :obj:`GamePlayer` object.
    :ivar black: The black player of the game. Holds the :obj:`GamePlayer` object.
    """

    url: Optional[str]
    pgn: Optional[str]
    time_control: Optional[str]
    end_time: Optional[int]
    start_time: Optional[int]
    rated: Optional[bool]
    fen: Optional[str]
    time_class: Optional[str]
    rules: Optional[str]
    match: Optional[str]

    white: Optional["GamePlayer"]
    black: Optional["GamePlayer"]

    def __post_init__(self):
        self.end_datetime = from_timestamp(self.end_time)
        self.start_datetime = from_timestamp(self.start_time)


@dataclass(repr=True)
class GamePlayer(object):
    """
    :ivar rating: The rating of the player.
    :ivar result: The result of the player.
    :ivar id: The ID of the player.
    :ivar username: The username of the player.
    :ivar uuid: The UUID of the player
    """

    rating: Optional[int]
    result: Optional[str]
    id: Optional[str]
    username: Optional[str]
    uuid: Optional[str]
