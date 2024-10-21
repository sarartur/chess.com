import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_player_profile.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_player_profile(username="fabianocaruana")
    validate_response(response)


@vcr.use_cassette("get_player_profile.yaml")
def test_with_client(client):
    response = client.get_player_profile(username="fabianocaruana")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_player_profile.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_player_profile(username="fabianocaruana")
    validate_response(response)


def validate_response(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    player = response.player
    assert isinstance(player.avatar, str)
    assert isinstance(player.player_id, int)
    assert isinstance(player.id, str)
    assert isinstance(player.url, str)
    assert isinstance(player.name, str)
    assert isinstance(player.username, str)
    assert isinstance(player.title, str)
    assert isinstance(player.followers, int)
    assert isinstance(player.country, str)
    assert isinstance(player.last_online, int)
    assert isinstance(player.joined, int)
    assert isinstance(player.status, str)
    assert isinstance(player.is_streamer, bool)
    assert isinstance(player.verified, bool)
    assert isinstance(player.league, str)
    assert isinstance(player.streaming_platforms, list)
