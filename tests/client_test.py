from unittest.mock import MagicMock, patch

from chessdotcom.client import ChessDotComClient, RateLimitHandler
from chessdotcom.types import Resource


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
    client = ChessDotComClient()

    mock_requests.get.return_value = MagicMock(
        status_code=200, text='{"name": "fabianocaruana"}'
    )

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
    assert response.json == {"name": "fabianocaruana"}


@patch("chessdotcom.client.requests")
def test_do_get_request_sync_combined_headers(mock_requests):
    client = ChessDotComClient(request_config={"headers": {"header": "value"}})

    mock_requests.get.return_value = MagicMock(status_code=200, text="{}")

    client.do_get_request(
        Resource(
            uri="/player/fabianocaruana",
            request_config={"headers": {"header": "override_value"}},
        )
    )

    assert mock_requests.get.called_once_with(
        url="https://api.chess.com/player/fabianocaruana",
        headers={"headers": {"header": "override_value"}},
        timeout=30,
    )


@patch("chessdotcom.client.requests")
def test_do_get_request_sync_top_level_attr(mock_requests):
    client = ChessDotComClient()

    mock_requests.get.return_value = MagicMock(status_code=200, text='{"key": "value"}')

    response = client.do_get_request(
        Resource(
            uri="/player/fabianocaruana",
            request_config={"headers": {"header": "override_value"}},
            top_level_attr="top_level_attr",
        )
    )

    assert mock_requests.get.called_once_with(
        url="https://api.chess.com/player/fabianocaruana",
        headers={"headers": {"header": "override_value"}},
        timeout=30,
    )
    assert response.top_level_attr.key == "value"
