from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_tournament_details(
    url_id: str, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`ChessDotComResponse` object containing details about a daily,
                live and arena tournament.
    """
    return Resource(
        uri=f"/tournament/{url_id}",
        tts=tts,
        top_level_attribute="tournament",
        request_options=request_options,
    )
