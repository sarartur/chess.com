"""
List of usernames for players who identify themselves as being in this country.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-country-players
"""

from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse


@Client.endpoint
def get_country_players(
    iso: str, tts=0, **request_options
) -> "GetCountryPlayersResponse":
    """
    :param iso: country's 2-character ISO 3166 code.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetCountryPlayersResponse` object containing a list of usernames for players
                who identify themselves as being in this country.
    """
    return Resource(
        uri=f"/country/{iso}/players",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetCountryPlayersResponse(
            json=data, text=text, players=self._build_players(data)
        )

    def _build_players(self, data):
        return [club for club in data.get("players", [])]


class GetCountryPlayersResponse(ChessDotComResponse):
    """
    :ivar players: Holds list of URLs for players.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json, text, players):
        super().__init__(json=json, text=text)
        self.players = players
