from dataclasses import dataclass

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_player_stats(username: str, tts=0, **request_options) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing information about the
                plyers's ratings, win/loss, and other stats.
    """
    return Resource(
        uri=f"/player/{username}/stats",
        tts=tts,
        top_level_attribute="stats",
        request_options=request_options,
    )


class GetPlayerStatsResponse(ChessDotComResponse):
    """
    :ivar stats: Holds the :obj:`PlayerStats` object.
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    """

    def __init__(self, json: dict, text: str, stats: "PlayerStats"):
        self.stats = stats
        self.json = json
        self.text = text


@dataclass(repr=True)
class PlayerStats(object):
    pass
