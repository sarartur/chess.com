import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_player_games_by_month_pgn.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_player_games_by_month_pgn(
        username="fabianocaruana", year="2020", month="05"
    )
    validate_response(response)


@vcr.use_cassette("get_player_games_by_month_pgn.yaml")
def test_with_client(client):
    response = client.get_player_games_by_month_pgn(
        username="fabianocaruana", year="2020", month="05"
    )
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_player_games_by_month_pgn.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_player_games_by_month_pgn(
        username="fabianocaruana", year="2020", month="05"
    )
    validate_response(response)


def validate_response(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    assert isinstance(response.pgn.pgn, str)
