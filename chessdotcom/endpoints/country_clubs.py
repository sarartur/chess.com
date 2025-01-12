from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_country_clubs(iso: str, tts=0, **request_options) -> ChessDotComResponse:
    """
    :param iso: country's 2-character ISO 3166 code.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of URLs for clubs identified
                as being in or associated with this country.
    """
    return Resource(
        uri=f"/country/{iso}/clubs", tts=tts, request_options=request_options
    )
