from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_tournament_round(
    url_id: str, round_num: int, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param round_num: the round of the tournament.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                 details about a tournament's round.
    """
    return Resource(
        uri=f"/tournament/{url_id}/{round_num}",
        tts=tts,
        top_level_attribute="tournament_round",
        request_options=request_options,
    )
