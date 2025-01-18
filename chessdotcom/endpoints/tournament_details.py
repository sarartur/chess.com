"""
Get details about a daily, live and arena tournament.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-tournament-profile
"""

from dataclasses import dataclass
from typing import List, Optional

from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse
from ..utils import dig, from_timestamp


@Client.endpoint
def get_tournament_details(
    url_id: str, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetTournamentDetailsResponse` object containing details about a daily,
                live and arena tournament.
    """
    return Resource(
        uri=f"/tournament/{url_id}",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetTournamentDetailsResponse(
            json={"tournament": data},
            text=text,
            tournament=TournamentDetails(
                name=data.get("name"),
                url=data.get("url"),
                description=data.get("description"),
                creator=data.get("creator"),
                status=data.get("status"),
                finish_time=data.get("finish_time"),
                settings=TournamentSettings(
                    type=dig(data, ("settings", "type")),
                    rules=dig(data, ("settings", "rules")),
                    is_rated=dig(data, ("settings", "is_rated")),
                    is_official=dig(data, ("settings", "is_official")),
                    is_invite_only=dig(data, ("settings", "is_invite_only")),
                    min_rating=dig(data, ("settings", "min_rating")),
                    max_rating=dig(data, ("settings", "max_rating")),
                    initial_group_size=dig(data, ("settings", "initial_group_size")),
                    user_advance_count=dig(data, ("settings", "user_advance_count")),
                    use_tiebreak=dig(data, ("settings", "use_tiebreak")),
                    allow_vacation=dig(data, ("settings", "allow_vacation")),
                    winner_places=dig(data, ("settings", "winner_places")),
                    registered_user_count=dig(
                        data, ("settings", "registered_user_count")
                    ),
                    games_per_opponent=dig(data, ("settings", "games_per_opponent")),
                    total_rounds=dig(data, ("settings", "total_rounds")),
                    concurrent_games_per_opponent=dig(
                        data, ("settings", "concurrent_games_per_opponent")
                    ),
                    time_class=dig(data, ("settings", "time_class")),
                    time_control=dig(data, ("settings", "time_control")),
                ),
                players=[
                    TournamentPlayer(
                        username=player.get("username"),
                        status=player.get("status"),
                    )
                    for player in data.get("players", [])
                ],
                rounds=data.get("rounds", []),
            ),
        )


class GetTournamentDetailsResponse(ChessDotComResponse):
    """
    :ivar tournament: Holds the :obj:`TournamentDetails` object.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json, text, tournament):
        super().__init__(json=json, text=text)
        self.tournament = tournament


@dataclass(repr=True)
class TournamentDetails(object):
    """
    :ivar name: Tournament's name.
    :ivar url: URL for the tournament's web page on www.chess.com.
    :ivar description: Tournament's description.
    :ivar creator: The creator of the tournament.
    :ivar status: The status of the tournament.
    :ivar finish_time: The time the tournament finishes.
    :ivar settings: The tournament settings. Holds :obj:`TournamentSettings` object.
    :ivar players: List of :obj:`TournamentPlayer` objects.
    :ivar rounds: List of rounds in the tournament.
    :ivar finish_datetime: The finish time as a datetime object.
    """

    name: Optional[str]
    url: Optional[str]
    description: Optional[str]
    creator: Optional[str]
    status: Optional[str]
    finish_time: Optional[int]
    settings: "TournamentSettings"
    players: List["TournamentPlayer"]
    rounds: List[str]

    def __post_init__(self):
        self.finish_datetime = from_timestamp(self.finish_time)


@dataclass(repr=True)
class TournamentSettings(object):
    """
    :ivar type: The type of the tournament.
    :ivar rules: The rules of the tournament.
    :ivar is_rated: Whether the tournament is rated.
    :ivar is_official: Whether the tournament is official.
    :ivar is_invite_only: Whether the tournament is invite-only.
    :ivar min_rating: The minimum rating required to join the tournament.
    :ivar max_rating: The maximum rating required to join the tournament.
    :ivar initial_group_size: The initial group size of the tournament.
    :ivar user_advance_count: The user advance count of the tournament.
    :ivar use_tiebreak: Whether the tournament uses tiebreak.
    :ivar allow_vacation: Whether the tournament allows vacation.
    :ivar winner_places: The number of winner places in the tournament.
    :ivar registered_user_count: The number of registered users in the tournament.
    :ivar games_per_opponent: The number of games per opponent in the tournament.
    :ivar total_rounds: The total number of rounds in the tournament.
    :ivar concurrent_games_per_opponent: The number of concurrent games per opponent.
    :ivar time_class: The time control class of the tournament.
    :ivar time_control: The time control of the tournament.
    """

    type: Optional[str]
    rules: Optional[str]
    is_rated: Optional[bool]
    is_official: Optional[bool]
    is_invite_only: Optional[bool]
    min_rating: Optional[int]
    max_rating: Optional[int]
    initial_group_size: Optional[int]
    user_advance_count: Optional[int]
    use_tiebreak: Optional[bool]
    allow_vacation: Optional[bool]
    winner_places: Optional[int]
    registered_user_count: Optional[int]
    games_per_opponent: Optional[int]
    total_rounds: Optional[int]
    concurrent_games_per_opponent: Optional[int]
    time_class: Optional[str]
    time_control: Optional[str]


@dataclass(repr=True)
class TournamentPlayer(object):
    """
    :ivar username: The username of the player.
    :ivar status: The status of the player
    """

    username: Optional[str]
    status: Optional[str]
