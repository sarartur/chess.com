from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder


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


class ResponseBuilder(ResponseBuilder):
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
        self.json = json
        self.text = text
        self.players = players
