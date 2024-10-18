import pytest

from chessdotcom import ChessDotComClient, Client
from chessdotcom import endpoints as _endpoints


@pytest.fixture(scope="session", autouse=True)
def set_headers():
    Client.request_config["headers"][
        "User-Agent"
    ] = "chess.com wrapper testing scripts. https://github.com/sarartur/chess.com"

    Client.request_config["headers"]["Accept-Encoding"] = None


@pytest.fixture
def client():
    return ChessDotComClient(aio=False)


@pytest.fixture
def async_client():
    return ChessDotComClient(aio=True)


@pytest.fixture
def endpoints():
    return _endpoints
