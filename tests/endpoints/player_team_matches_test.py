from unittest.mock import patch

import pytest

from chessdotcom.endpoints.player_team_matches import TeamMatches
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
@vcr.use_cassette("get_player_team_matches.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_player_team_matches(username="akshayraj_kore")
    validate_response(response)


@vcr.use_cassette("get_player_team_matches.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_player_team_matches(username="akshayraj_kore")

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)
    assert isinstance(response.matches, TeamMatches)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("matches") is not None

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
