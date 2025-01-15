from chessdotcom.client import Client, Resource
from chessdotcom.response_builder import ChessDotComResponse


@Client.endpoint
def get_team_match_board(
    match_id: int, board_num: int, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param match_id: the id of the match.
    :param board_num: the number of the board.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                details about a team match board.
    """
    return Resource(
        uri=f"/match/{match_id}/{board_num}",
        tts=tts,
        top_level_attribute="match_board",
        request_options=request_options,
    )
