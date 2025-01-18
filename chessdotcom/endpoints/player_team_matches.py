from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_player_team_matches(
    username: str, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of team matches
                the player has attended,
                is participating or is currently registered.
    """
    return Resource(
        uri=f"/player/{username}/matches",
        tts=tts,
        top_level_attribute="matches",
        request_options=request_options,
    )
