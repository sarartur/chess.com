from dataclasses import dataclass
from typing import Optional

from chessdotcom.client import Client, Resource
from chessdotcom.response_builder import ChessDotComResponse, ResponseBuilder


@Client.endpoint
def get_team_match_board(
    match_id: int, board_num: int, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param match_id: the id of the match.
    :param board_num: the number of the board.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                details about a team match board.
    """
    return Resource(
        uri=f"/match/{match_id}/{board_num}",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(ResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetTeamMatchBoardResponse(
            json={"match_board": data},
            text=text,
            match_board=MatchBoard(
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
                ]
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
        self.json = json
        self.text = text
        self.match_board = match_board


@dataclass(repr=True)
class MatchBoard(object):
    games: list["Game"]


@dataclass(repr=True)
class Game(object):
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


@dataclass(repr=True)
class GamePlayer(object):
    rating: Optional[int]
    result: Optional[str]
    id: Optional[str]
    username: Optional[str]
    uuid: Optional[str]
