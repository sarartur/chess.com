"""
List of URLs for clubs identified as being in or associated with this country.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-country-clubs
"""

from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse


@Client.endpoint
def get_country_clubs(iso: str, tts=0, **request_options) -> "GetCountryClubsResponse":
    """
    :param iso: country's 2-character ISO 3166 code.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetCountryClubsResponse` object containing a list of URLs for clubs identified
                as being in or associated with this country.
    """
    return Resource(
        uri=f"/country/{iso}/clubs",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetCountryClubsResponse(
            json=data, text=text, clubs=self._build_clubs(data)
        )

    def _build_clubs(self, data):
        return [club for club in data.get("clubs", [])]


class GetCountryClubsResponse(ChessDotComResponse):
    """
    :ivar clubs: Holds list of URLs for clubs.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json, text, clubs):
        super().__init__(json=json, text=text)
        self.clubs = clubs
