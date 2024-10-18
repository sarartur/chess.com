import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_player_team_matches.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_player_team_matches(username="akshayraj_kore")
    validate_response(response)


@vcr.use_cassette("get_player_team_matches.yaml")
def test_with_client(client):
    response = client.get_player_team_matches(username="akshayraj_kore")
    validate_response(response)


@pytest.mark.asyncio
async def test_with_async_client(async_client):
    with vcr.use_cassette("get_player_team_matches.yaml"):
        response = await async_client.get_player_team_matches(username="akshayraj_kore")

    validate_response(response)


def validate_response(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    matches = response.matches
    for match in matches.finished:
        assert isinstance(match.name, str)
        assert isinstance(match.url, str)
        assert isinstance(match.id, str)
        assert isinstance(match.club, str)
        assert isinstance(match.results.played_as_white, str)
        assert isinstance(match.results.played_as_black, str)
        assert isinstance(match.board, str)

    for match in matches.in_progress:
        assert isinstance(match.name, str)
        assert isinstance(match.url, str)
        assert isinstance(match.id, str)
        assert isinstance(match.club, str)
        assert isinstance(match.board, str)

    for match in matches.registered:
        assert isinstance(match.name, str)
        assert isinstance(match.url, str)
        assert isinstance(match.id, str)
        assert isinstance(match.club, str)
