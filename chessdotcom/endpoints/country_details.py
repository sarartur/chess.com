"""
Additional details about a country.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-country-profile
"""

from dataclasses import dataclass
from typing import Optional

from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse


@Client.endpoint
def get_country_details(
    iso: str, tts=0, **request_options
) -> "GetCountryDetailsResponse":
    """
    :param iso: country's 2-character ISO 3166 code.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetCountryDetailsResponse`` object containing
                additional details about a country.
    """
    return Resource(
        uri=f"/country/{iso}",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetCountryDetailsResponse(
            json={"country": data},
            text=text,
            country=CountryDetails(
                name=data.get("name"), id=data.get("@id"), code=data.get("code")
            ),
        )


class GetCountryDetailsResponse(ChessDotComResponse):
    """
    :ivar country: Holds the :obj:`CountryDetails` object.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json, text, country):
        super().__init__(json=json, text=text)
        self.country = country


@dataclass(repr=True)
class CountryDetails(object):
    """
    :ivar name: Country's name.
    :ivar id: The URL of the country's profile
    :ivar code: The ISO-3166-1 2-character code.
    """

    name: Optional[str]
    id: Optional[str]
    code: Optional[str]
