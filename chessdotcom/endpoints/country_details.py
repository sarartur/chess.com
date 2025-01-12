from ..client import Client, Resource
from ..response_builder import ChessDotComResponse


@Client.endpoint
def get_country_details(iso: str, tts=0, **request_options) -> ChessDotComResponse:
    """
    :param iso: country's 2-character ISO 3166 code.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                additional details about a country.
    """
    return Resource(
        uri=f"/country/{iso}",
        tts=tts,
        top_level_attribute="country",
        request_options=request_options,
    )
