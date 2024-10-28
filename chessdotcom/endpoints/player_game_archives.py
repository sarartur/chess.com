"""
Game archives available for this player.

API doc: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-games-archive-list
"""


from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder


@Client.endpoint
def get_player_game_archives(
    username: str, tts=0, **request_options
) -> "GetPlayerGameArchivesResponse":
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetPlayerGameArchivesResponse` object containing a
                list of monthly archives available for this player.
    """
    return Resource(
        uri=f"/player/{username}/games/archives",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(ResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetPlayerGameArchivesResponse(
            json=data,
            text=text,
            archives=data.get("archives", []),
        )


class GetPlayerGameArchivesResponse(ChessDotComResponse):
    """
    :ivar archives: array of URLs for monthly archives in ascending chronological order.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json: dict, text: str, archives: list) -> None:
        self.archives = archives
        self.json = json
        self.text = text
