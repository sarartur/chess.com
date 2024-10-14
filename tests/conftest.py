import pytest

from chessdotcom import Client


@pytest.fixture(scope="session", autouse=True)
def set_headers():
    Client.default_request_options["headers"][
        "user-agent"
    ] = "chess.com wrapper testing scripts. https://github.com/sarartur/chess.com"
