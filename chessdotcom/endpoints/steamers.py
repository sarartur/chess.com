from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_streamers(tts=0, **request_options) -> ChessDotComResponse:
    """
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`ChessDotComResponse` object containing
                information about Chess.com streamers.
    """
    return Resource(uri="/streamers", tts=tts, request_options=request_options)
