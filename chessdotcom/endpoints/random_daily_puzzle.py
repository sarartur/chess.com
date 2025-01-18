from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_random_daily_puzzle(tts=0, **request_options) -> ChessDotComResponse:
    """
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                information about a randomly picked daily puzzle.
    """
    return Resource(
        uri="/puzzle/random",
        tts=tts,
        top_level_attribute="puzzle",
        request_options=request_options,
    )
