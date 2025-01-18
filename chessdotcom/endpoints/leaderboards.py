from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_leaderboards(tts=0, **request_options) -> ChessDotComResponse:
    """
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`ChessDotComResponse` object containing
                information about top 50 player for daily and live games, tactics and lessons.
    """
    return Resource(
        uri="/leaderboards",
        tts=tts,
        top_level_attribute="leaderboards",
        request_options=request_options,
    )
