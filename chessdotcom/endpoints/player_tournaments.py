from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_player_tournaments(
    username: str, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a
                list of tournaments the player is registered,
                is attending or has attended in the past.
    """
    return Resource(
        uri=f"/player/{username}/tournaments",
        tts=tts,
        top_level_attribute="tournaments",
        request_options=request_options,
    )
