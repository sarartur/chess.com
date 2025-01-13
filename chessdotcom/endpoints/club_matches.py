from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder
from ..utils import from_timestamp


@Client.endpoint
def get_club_matches(url_id: str, tts=0, **request_options) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of daily and club matches.
    """
    return Resource(
        uri=f"/club/{url_id}/matches",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(ResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetClubMatchesResponse(
            json={"matches": data}, text=text, matches=self._build_club_matches(data)
        )

    def _build_club_matches(self, data):
        return ClubMatches(
            finished=self._build_matches(data.get("finished", [])),
            in_progress=self._build_matches(data.get("in_progress", [])),
            registered=self._build_matches(data.get("registered", [])),
        )

    def _build_matches(self, data):
        return [
            ClubMatch(
                name=d.get("name"),
                id=d.get("@id"),
                opponent=d.get("opponent"),
                start_time=d.get("start_time"),
                time_class=d.get("time_class"),
                result=d.get("result"),
            )
            for d in data
        ]


class GetClubMatchesResponse(ChessDotComResponse):
    """
    :ivar matches: Holds the list of daily and club matches.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json, text, matches):
        self.json = json
        self.text = text
        self.matches = matches


@dataclass(repr=True)
class ClubMatches(object):
    finished: list
    in_progress: list
    registered: list


@dataclass(repr=True)
class ClubMatch(object):
    name: Optional[str]
    id: Optional[str]
    opponent: Optional[str]
    start_time: Optional[int]
    time_class: Optional[str]
    result: Optional[str]

    def __post_init__(self):
        self.start_datetime = from_timestamp(self.start_time)
