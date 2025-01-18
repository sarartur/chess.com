from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_titled_players(
    title_abbrev: str, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param title_abbrev: abbreviation of chess title.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`ChessDotComResponse` object containing a list of usernames.
    """
    return Resource(
        uri=f"/titled/{title_abbrev}", tts=tts, request_options=request_options
    )
