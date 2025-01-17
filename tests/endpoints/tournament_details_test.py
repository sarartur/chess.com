from unittest.mock import patch

import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_tournament_details.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_tournament_details(
        url_id="-33rd-chesscom-quick-knockouts-1401-1600"
    )
    validate_response(response)


@vcr.use_cassette("get_tournament_details.yaml")
def test_with_client(client):
    response = client.get_tournament_details(
        url_id="-33rd-chesscom-quick-knockouts-1401-1600"
    )
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_tournament_details.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_tournament_details(
        url_id="-33rd-chesscom-quick-knockouts-1401-1600"
    )
    validate_response(response)


@vcr.use_cassette("get_tournament_details.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_tournament_details(
        url_id="-33rd-chesscom-quick-knockouts-1401-1600"
    )

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("tournament") is not None

    tournament = response.tournament

    assert isinstance(tournament.name, str)
    assert isinstance(tournament.url, str)
    assert isinstance(tournament.description, str)
    assert isinstance(tournament.creator, str)
    assert isinstance(tournament.status, str)
    assert isinstance(tournament.finish_time, int)
    assert isinstance(tournament.settings.type, str)
    assert isinstance(tournament.settings.rules, str)
    assert isinstance(tournament.settings.is_rated, bool)
    assert isinstance(tournament.settings.is_official, bool)
    assert isinstance(tournament.settings.is_invite_only, bool)
    assert isinstance(tournament.settings.min_rating, int)
    assert isinstance(tournament.settings.max_rating, int)
    assert isinstance(tournament.settings.initial_group_size, int)
    assert isinstance(tournament.settings.user_advance_count, int)
    assert isinstance(tournament.settings.use_tiebreak, bool)
    assert isinstance(tournament.settings.allow_vacation, bool)
    assert isinstance(tournament.settings.winner_places, int)
    assert isinstance(tournament.settings.registered_user_count, int)
    assert isinstance(tournament.settings.games_per_opponent, int)
    assert isinstance(tournament.settings.total_rounds, int)
    assert isinstance(tournament.settings.concurrent_games_per_opponent, int)
    assert isinstance(tournament.settings.time_class, str)
    assert isinstance(tournament.settings.time_control, str)

    for player in tournament.players:
        assert isinstance(player.username, str)
        assert isinstance(player.status, str)

    assert all(isinstance(round, str) for round in tournament.rounds)
