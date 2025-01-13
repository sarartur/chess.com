from dataclasses import dataclass

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder


@Client.endpoint
def get_club_members(url_id: str, tts=0, **request_options) -> "GetClubMembersResponse":
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetClubMembersResponse`` object containing a list of club members.
    """
    return Resource(
        uri=f"/club/{url_id}/members",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(ResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetClubMembersResponse(
            json=data, text=text, members=self._build_members(data)
        )

    def _build_members(self, data):
        return ClubMembers(
            weekly=self._build_member_details(data.get("weekly", [])),
            monthly=self._build_member_details(data.get("monthly", [])),
            all_time=self._build_member_details(data.get("all_time", [])),
        )

    def _build_member_details(self, data):
        return [
            ClubMembersDetails(username=d.get("username"), joined=d.get("joined"))
            for d in data
        ]


class GetClubMembersResponse(ChessDotComResponse):
    """
    :ivar members: Holds the :obj:`ClubMembers` object.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json, text, members):
        self.json = json
        self.text = text
        self.members = members


@dataclass(repr=True)
class ClubMembers(object):
    weekly: list
    monthly: list
    all_time: list


@dataclass(repr=True)
class ClubMembersDetails(object):
    username: str
    joined: int
