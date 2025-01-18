from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_current_daily_puzzle(tts=0, **request_options) -> ChessDotComResponse:
    """
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`ChessDotComResponse` object containing
                information about the daily puzzle found in www.chess.com.
    """
    return Resource(
        uri="/puzzle",
        top_level_attribute="puzzle",
        tts=tts,
        request_options=request_options,
    )
