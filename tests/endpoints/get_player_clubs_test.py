import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_player_clubs.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_player_clubs(username="fabianocaruana")
    validate_response(response)


@vcr.use_cassette("get_player_clubs.yaml")
def test_with_client(client):
    response = client.get_player_clubs(username="fabianocaruana")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_player_clubs.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_player_clubs(username="fabianocaruana")
    validate_response(response)


def validate_response(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    for club in response.clubs:
        assert isinstance(club.id, str)
        assert isinstance(club.name, str)
        assert isinstance(club.last_activity, int)
        assert isinstance(club.icon, str)
        assert isinstance(club.url, str)
        assert isinstance(club.joined, int)
