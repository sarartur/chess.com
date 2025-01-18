"""
Get ratings, win/loss, and other stats about a player's game play, tactics,
lessons and Puzzle Rush score.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-titled
"""


from ..client import Client, Resource
from ..response_builder import BaseResponseBuilder, ChessDotComResponse


@Client.endpoint
def get_titled_players(
    title_abbrev: str, tts=0, **request_options
) -> "GetTitledPlayersResponse":
    """
    :param title_abbrev: abbreviation of chess title.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetTitledPlayersResponse` object containing a list of usernames.
    """
    return Resource(
        uri=f"/titled/{title_abbrev}",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(BaseResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetTitledPlayersResponse(
            json=data,
            text=text,
            players=data.get("players", []),
        )


class GetTitledPlayersResponse(ChessDotComResponse):
    """
    :ivar players: List of usernames.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json, text, players):
        super().__init__(json=json, text=text)
        self.players = players
