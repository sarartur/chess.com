"""
Get additional details about a club.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-club-profile
"""


from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse
from ..utils import from_timestamp


@Client.endpoint
def get_club_details(url_id: str, tts=0, **request_options) -> "GetClubDetailsResponse":
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetClubDetailsResponse` object containing additional details about a club.
    """
    return Resource(
        uri=f"/club/{url_id}",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetClubDetailsResponse(
            json={"club": data},
            text=text,
            club=ClubDetails(
                name=data.get("name"),
                url=data.get("url"),
                icon=data.get("icon"),
                country=data.get("country"),
                id=data.get("@id"),
                club_id=data.get("club_id"),
                average_daily_rating=data.get("average_daily_rating"),
                members_count=data.get("members_count"),
                created=data.get("created"),
                last_activity=data.get("last_activity"),
                admin=data.get("admin", []),
                visibility=data.get("visibility"),
                join_request=data.get("join_request"),
                description=data.get("description"),
            ),
        )


class GetClubDetailsResponse(ChessDotComResponse):
    """
    :ivar club: Holds the :obj:`ClubDetails` object.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json, text, club):
        super().__init__(json=json, text=text)
        self.club = club


@dataclass(repr=True)
class ClubDetails(object):
    """
    :ivar name: Club's name.
    :ivar url: URL for the club's web page on www.chess.com.
    :ivar icon: URL for the club's icon.
    :ivar country: Country's name.
    :ivar id: The URL of the club's profile.
    :ivar club_id: The club's ID.
    :ivar average_daily_rating: The club's average daily rating.
    :ivar members_count: The number of members in the club.
    :ivar created: The time the club was created.
    :ivar last_activity: The time of the club's last activity.
    :ivar admin: List of club admins.
    :ivar visibility: The club's visibility setting.
    :ivar join_request: The club's join request setting.
    :ivar description: The club's description.
    :ivar last_activity_datetime: The last activity as a datetime object.
    :ivar created_datetime: The created timestamp as a datetime object.
    """

    name: Optional[str]
    url: Optional[str]
    icon: Optional[str]
    country: Optional[str]
    id: Optional[str]
    club_id: Optional[int]
    average_daily_rating: Optional[int]
    members_count: Optional[int]
    created: Optional[int]
    last_activity: Optional[int]
    admin: Optional[list]
    visibility: Optional[str]
    join_request: Optional[str]
    description: Optional[str]

    def __post_init__(self):
        self.last_activity_datetime = from_timestamp(self.last_activity)
        self.created_datetime = from_timestamp(self.created)
