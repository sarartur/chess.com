import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_player_game_archives.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_player_game_archives(username="afgano29")
    validate_response(response)


@vcr.use_cassette("get_player_game_archives.yaml")
def test_with_client(client):
    response = client.get_player_game_archives(username="afgano29")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_player_game_archives.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_player_game_archives(username="afgano29")
    validate_response(response)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("archives") is not None

    archives = response.archives
    assert all(isinstance(url, str) for url in archives)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)
    assert isinstance(response.archives, list)
