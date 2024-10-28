from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_player_current_games(
    username: str, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of Daily Chess games
                that a player is currently playing.
    """
    return Resource(
        uri=f"/player/{username}/games", tts=tts, request_options=request_options
    )
