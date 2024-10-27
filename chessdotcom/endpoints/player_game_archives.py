from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_player_game_archives(
    username: str, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a
                list of monthly archives available for this player.
    """
    return Resource(
        uri=f"/player/{username}/games/archives",
        tts=tts,
        request_options=request_options,
    )
