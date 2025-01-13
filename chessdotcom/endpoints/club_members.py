from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_club_members(url_id: str, tts=0, **request_options) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`ChessDotComResponse`` object containing a list of club members.
    """
    return Resource(
        uri=f"/club/{url_id}/members",
        tts=tts,
        top_level_attribute="members",
        request_options=request_options,
    )
