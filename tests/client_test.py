import json
from unittest.mock import MagicMock, patch

import pytest

from chessdotcom.client import ChessDotComClient, Client, RateLimitHandler, Resource
from chessdotcom.errors import ChessDotComClientError, ChessDotComDecodingError
from tests.support.aio_mock_response import AioMockResponse


@patch("chessdotcom.client.time.sleep")
def test_rate_limit_handler(sleep_mock):
    handler = RateLimitHandler(
        retries=2,
        tts=4,
    )

    assert (
        handler.should_try_again(status_code=429, resource=Resource(times_requested=0))
        is True
    )
    sleep_mock.assert_called_once_with(4)

    assert (
        handler.should_try_again(status_code=429, resource=Resource(times_requested=2))
        is True
    )
    assert (
        handler.should_try_again(status_code=429, resource=Resource(times_requested=3))
        is False
    )
    assert (
        handler.should_try_again(status_code=400, resource=Resource(times_requested=0))
        is False
    )


@patch("chessdotcom.client.requests")
def test_do_get_request_sync(mock_requests):
    mock_data = {"name": "fabianocaruana"}
    mock_requests.get.return_value = MagicMock(
        status_code=200, text=json.dumps(mock_data)
    )

    client = ChessDotComClient()
    response = client.do_get_request(
        Resource(
            uri="/player/fabianocaruana",
        )
    )

    assert mock_requests.get.called_once_with(
        url="https://api.chess.com/player/fabianocaruana",
        headers={},
        timeout=30,
    )
    assert response.name == "fabianocaruana"
    assert response.json == mock_data


@patch("chessdotcom.client.requests")
def test_do_get_request_sync_error(mock_requests):
    mock_data = {"message": "does not exist"}
    mock_requests.get.return_value = MagicMock(
        status_code=404,
        text=json.dumps(mock_data),
        headers={"Content-Type": "application/json"},
    )

    client = ChessDotComClient()

    with pytest.raises(ChessDotComClientError) as err:
        client.do_get_request(
            Resource(
                uri="/player/fabianocaruana",
            )
        )

    assert mock_requests.get.called_once_with(
        url="https://api.chess.com/player/fabianocaruana",
        headers={},
        timeout=30,
    )

    assert err.value.status_code == 404
    assert err.value.text == json.dumps(mock_data)
    assert err.value.json == mock_data
    assert err.value.headers == {"Content-Type": "application/json"}


@pytest.mark.asyncio
@patch("chessdotcom.client.ClientSession.get")
async def test_do_get_request_async(mock_session_get):
    mock_data = {"name": "fabianocaruana"}
    mock_session_get.return_value = AioMockResponse(
        text=json.dumps(mock_data), status=200
    )

    client = ChessDotComClient(aio=True)
    response = await client.do_get_request(
        Resource(
            uri="/player/fabianocaruana",
        )
    )

    assert mock_session_get.get.called_once_with(
        url="https://api.chess.com/player/fabianocaruana",
        headers={},
    )
    assert response.name == "fabianocaruana"
    assert response.json == {"name": "fabianocaruana"}


@pytest.mark.asyncio
@patch("chessdotcom.client.ClientSession.get")
async def test_do_get_request_async_error(mock_session_get):
    mock_data = {"message": "does not exist"}
    mock_session_get.return_value = AioMockResponse(
        text=json.dumps(mock_data),
        status=404,
        headers={"Content-Type": "application/json"},
    )

    client = ChessDotComClient(aio=True)

    with pytest.raises(ChessDotComClientError) as err:
        await client.do_get_request(
            Resource(
                uri="/player/fabianocaruana",
            )
        )

    assert err.value.status_code == 404
    assert err.value.text == json.dumps(mock_data)
    assert err.value.json == mock_data
    assert err.value.headers == {"Content-Type": "application/json"}


@patch("chessdotcom.client.requests")
def test_do_get_request_sync_decoding_error(mock_requests):
    mock_requests.get.return_value = MagicMock(
        status_code=200,
        text='{"key": ',
    )

    client = ChessDotComClient()

    with pytest.raises(ChessDotComDecodingError) as err:
        client.do_get_request(Resource(uri="/player/fabianocaruana"))

    assert err.value.text == '{"key": '


@patch("chessdotcom.client.requests")
def test_do_get_request_sync_combined_headers(mock_requests):
    client = ChessDotComClient(request_config={"headers": {"header": "value"}})

    mock_requests.get.return_value = MagicMock(status_code=200, text="{}")

    client.do_get_request(
        Resource(
            uri="/player/fabianocaruana",
            request_options={"headers": {"header": "override_value"}},
        )
    )

    assert mock_requests.get.called_once_with(
        url="https://api.chess.com/player/fabianocaruana",
        headers={"headers": {"header": "override_value"}},
        timeout=30,
    )


@patch("chessdotcom.client.requests")
def test_do_get_request_sync_top_level_attribute(mock_requests):
    client = ChessDotComClient()

    mock_requests.get.return_value = MagicMock(status_code=200, text='{"key": "value"}')

    response = client.do_get_request(
        Resource(
            uri="/player/fabianocaruana",
            request_options={"headers": {"header": "override_value"}},
            top_level_attribute="top_level_attribute",
        )
    )

    assert mock_requests.get.called_once_with(
        url="https://api.chess.com/player/fabianocaruana",
        headers={"headers": {"header": "override_value"}},
        timeout=30,
    )
    assert response.top_level_attribute.key == "value"


@patch("chessdotcom.client.requests")
def test_do_get_request_includes_user_agent_header(mock_requests):
    client = ChessDotComClient(user_agent="My Python Application. Contact me at...")

    mock_requests.get.return_value = MagicMock(status_code=200, text='{"key": "value"}')

    client.do_get_request(
        Resource(
            uri="/player/fabianocaruana",
            request_options={"headers": {"header": "override_value"}},
        )
    )

    assert mock_requests.get.called_once_with(
        url="https://api.chess.com/player/fabianocaruana",
        headers={"headers": {"User-Agent": "My Python Application. Contact me at..."}},
        timeout=30,
    )


def test_client_includes_default_config():
    old_config = {
        "aio": Client.aio,
        "request_config": Client.request_config,
        "rate_limit_handler": Client.rate_limit_handler,
    }

    Client.aio = True
    Client.request_config = {"some": "config"}
    Client.rate_limit_handler = "Some handler"

    try:
        client = ChessDotComClient()
    except Exception:
        raise "Error creating client"
    else:
        assert client.aio is False  # this is always overridden
        assert client.request_config == {"some": "config", "verify": True}
        assert client.rate_limit_handler == "Some handler"
    finally:
        Client.aio = old_config["aio"]
        Client.request_config = old_config["request_config"]
        Client.rate_limit_handler = old_config["rate_limit_handler"]


def test_client_combines_with_defaults():
    default_config = Client.request_config

    client = ChessDotComClient(
        aio=True,
        request_config={"some": "config"},
        rate_limit_handler="Some handler",
    )

    assert client.aio is True
    assert client.request_config == {
        **default_config,
        **{"some": "config"},
        "verify_ssl": True,
    }
    assert client.rate_limit_handler == "Some handler"


def test_verify_ssl_option():
    client = ChessDotComClient(verify_ssl=True)

    assert client.request_config["verify"] is True

    client = ChessDotComClient(verify_ssl=False)

    assert client.request_config["verify"] is False
