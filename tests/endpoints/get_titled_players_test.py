import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_titled_players.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_titled_players(title_abbrev="GM")
    validate_response(response)


@vcr.use_cassette("get_titled_players.yaml")
def test_with_client(client):
    response = client.get_titled_players(title_abbrev="GM")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_titled_players.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_titled_players(title_abbrev="GM")
    validate_response(response)


def validate_response(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    players = response.players
    assert isinstance(players, list)
    assert all(isinstance(player, str) for player in players)
