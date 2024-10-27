from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_player_clubs(username: str, tts=0, **request_options) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
            a list of clubs the player is a member of.
    """
    return Resource(
        uri=f"/player/{username}/clubs", tts=tts, request_options=request_options
    )
