from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_team_match(match_id: int, tts=0, **request_options) -> ChessDotComResponse:
    """
    :param match_id: the id of the match.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                details about a team match and players playing that match.
    """
    return Resource(
        uri=f"/match/{match_id}",
        tts=tts,
        top_level_attribute="match",
        request_options=request_options,
    )
