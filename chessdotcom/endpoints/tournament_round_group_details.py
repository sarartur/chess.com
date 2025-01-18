"""
Get details about a tournament's round group.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-tournament-round-group
"""


from dataclasses import dataclass
from typing import List, Optional, Union

from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse
from ..utils import from_timestamp


@Client.endpoint
def get_tournament_round_group_details(
    url_id: str, round_num: int, group_num: int, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param round_num: the round of the tournament.
    :param group_num: the group in the tournament.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`ChessDotComResponse` object containing
                details about a tournament's round group.
    """
    return Resource(
        uri=f"/tournament/{url_id}/{round_num}/{group_num}",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetTournamentRoundGroupDetailsResponse(
            json={"tournament_round_group": data},
            text=text,
            tournament_round_group=TournamentRoundGroup(
                players=[
                    TournamentPlayer(
                        username=player.get("username"),
                        points=player.get("points"),
                        is_advancing=player.get("is_advancing"),
                        tie_break=player.get("tie_break"),
                    )
                    for player in data.get("players", [])
                ],
                games=[
                    TournamentGames(
                        url=game.get("url"),
                        pgn=game.get("pgn"),
                        time_control=game.get("time_control"),
                        end_time=game.get("end_time"),
                        rated=game.get("rated"),
                        fen=game.get("fen"),
                        start_time=game.get("start_time"),
                        time_class=game.get("time_class"),
                        rules=game.get("rules"),
                        move_by=game.get("move_by"),
                        last_activity=game.get("last_activity"),
                        draw_offer=game.get("draw_offer"),
                        white=self._build_game_player(game.get("white")),
                        black=self._build_game_player(game.get("black")),
                    )
                    for game in data.get("games", [])
                ],
                fair_play_removals=data.get("fair_play_removals", []),
            ),
        )

    def _build_game_player(self, data):
        if not data:
            return

        return GamePlayer(
            rating=data.get("rating"),
            result=data.get("result"),
            id=data.get("@id"),
            username=data.get("username"),
            uuid=data.get("uuid"),
        )


class GetTournamentRoundGroupDetailsResponse(ChessDotComResponse):
    """
    :ivar tournament_round_group: Holds the :obj:`TournamentRoundGroup` object.
    :ivar json: The JSON response from the API.
    :ivar text: The raw response from the API.
    """

    def __init__(self, tournament_round_group, json, text):
        super().__init__(json=json, text=text)
        self.tournament_round_group = tournament_round_group


@dataclass(repr=True)
class TournamentRoundGroup(object):
    """
    :ivar players: List of :obj:`TournamentPlayer` objects.
    :ivar games: List of :obj:`TournamentGames` objects.
    :ivar fair_play_removals: List of usernames removed for fair play violations.
    """

    players: List["TournamentPlayer"]
    games: List["TournamentGames"]
    fair_play_removals: List[str]


@dataclass(repr=True)
class TournamentPlayer(object):
    """
    :ivar username: username of the player.
    :ivar points: the player's points.
    :ivar is_advancing: whether the player is advancing to the next round.
    :ivar tie_break: the player's tie-break score.
    """

    username: Optional[str]
    points: Optional[Union[float, int]]
    is_advancing: Optional[bool]
    tie_break: Optional[Union[float, int]]


@dataclass(repr=True)
class TournamentGames(object):
    """
    :ivar url: URL for the game's web page on www.chess.com.
    :ivar pgn: the game's PGN.
    :ivar time_control: the game's time control.
    :ivar end_time: the time the game ends.
    :ivar rated: whether the game is rated.
    :ivar fen: the game's FEN.
    :ivar start_time: the time the game starts.
    :ivar time_class: the game's time class.
    :ivar rules: the game's rules.
    :ivar move_by: the time the player must move by.
    :ivar last_activity: the time of the game's last activity.
    :ivar draw_offer: the draw offer.
    :ivar end_datetime: the end time as a datetime object.
    :ivar start_datetime: the start time as a datetime object.
    :ivar last_activity_datetime: the last activity as a datetime object.
    :ivar move_by_datetime: the move by time as a datetime object.
    :ivar white: Holds the :obj:`GamePlayer` object for the white player.
    :ivar black: Holds the :obj:`GamePlayer` object for the black player.
    """

    url: Optional[str]
    pgn: Optional[str]
    time_control: Optional[str]
    end_time: Optional[int]
    rated: Optional[bool]
    fen: Optional[str]
    start_time: Optional[int]
    time_class: Optional[str]
    rules: Optional[str]
    move_by: Optional[int]
    last_activity: Optional[int]
    draw_offer: Optional[str]

    white: Optional["GamePlayer"]
    black: Optional["GamePlayer"]

    def __post_init__(self):
        self.end_datetime = from_timestamp(self.end_time)
        self.start_datetime = from_timestamp(self.start_time)
        self.last_activity_datetime = from_timestamp(self.last_activity)
        self.move_by_datetime = from_timestamp(self.move_by)


@dataclass(repr=True)
class GamePlayer(object):
    """
    :ivar rating: the player's rating.
    :ivar result: the player's result.
    :ivar id: the player's ID.
    :ivar username: the player's username.
    :ivar uuid: the player's UUID.
    """

    rating: Optional[int]
    result: Optional[str]
    id: Optional[str]
    username: Optional[str]
    uuid: Optional[str]
