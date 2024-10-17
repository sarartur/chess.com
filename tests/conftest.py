import pytest

from chessdotcom import ChessDotComClient, Client
from chessdotcom import endpoints as _endpoints


@pytest.fixture(scope="session", autouse=True)
def set_headers():
    Client.default_request_options["headers"][
        "user-agent"
    ] = "chess.com wrapper testing scripts. https://github.com/sarartur/chess.com"


@pytest.fixture
def client():
    return ChessDotComClient(aio=False)


@pytest.fixture
def endpoints():
    return _endpoints
