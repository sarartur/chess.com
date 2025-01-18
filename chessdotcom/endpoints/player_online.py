from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def is_player_online(username: str, tts=0, **request_options) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing infomation about
                whether or not a player is online
    """
    return Resource(
        uri=f"/player/{username}/is-online", tts=tts, request_options=request_options
    )
