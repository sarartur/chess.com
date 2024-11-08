from unittest.mock import patch

import pytest

from chessdotcom.endpoints.player_tournaments import Tournaments
from tests.vcr import vcr


@vcr.use_cassette("get_player_tournaments.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_player_tournaments(username="fabianocaruana")
    validate_response(response)


@vcr.use_cassette("get_player_tournaments.yaml")
def test_with_client(client):
    response = client.get_player_tournaments(username="fabianocaruana")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_player_tournaments.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_player_tournaments(username="fabianocaruana")
    validate_response(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)
    assert isinstance(response.tournaments, Tournaments)


@vcr.use_cassette("get_player_tournaments.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_player_tournaments(username="fabianocaruana")

    validate_response_structure(response)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("tournaments") is not None

    tournaments = response.tournaments
    for tournament in tournaments.finished:
        assert isinstance(tournament.url, str)
        assert isinstance(tournament.id, str)
        assert isinstance(tournament.wins, int)
        assert isinstance(tournament.losses, int)
        assert isinstance(tournament.draws, int)
        assert isinstance(tournament.placement, int)
        assert isinstance(tournament.status, str)
        assert isinstance(tournament.total_players, int)
        assert isinstance(tournament.time_class, str)
        assert isinstance(tournament.type, str)

    for tournament in tournaments.in_progress:
        assert isinstance(tournament.url, str)
        assert isinstance(tournament.id, str)
        assert isinstance(tournament.status, str)

    for tournament in tournaments.registered:
        assert isinstance(tournament.url, str)
        assert isinstance(tournament.id, str)
        assert isinstance(tournament.status, str)
