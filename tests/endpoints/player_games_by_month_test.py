from datetime import datetime
from unittest.mock import patch

import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_player_games_by_month.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_player_games_by_month(
        username="fabianocaruana", year="2020", month="05"
    )
    validate_response(response)


@vcr.use_cassette("get_player_games_by_month.yaml")
def test_with_client(client):
    response = client.get_player_games_by_month(
        username="fabianocaruana", year="2020", month="05"
    )
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_player_games_by_month.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_player_games_by_month(
        username="fabianocaruana", year="2020", month="05"
    )
    validate_response(response)


@vcr.use_cassette("get_player_games_by_month.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_player_games_by_month(
        username="fabianocaruana", year="2020", month="05"
    )

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)
    assert isinstance(response.games, list)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("games") is not None

    games = response.games
    assert len(games) > 0
    for game in games:
        assert isinstance(game.url, str)
        assert isinstance(game.pgn, str)
        assert isinstance(game.time_control, str)
        assert isinstance(game.end_time, int)
        assert isinstance(game.start_time, (int, type(None)))
        assert isinstance(game.accuracies.white, float)
        assert isinstance(game.accuracies.black, float)
        assert isinstance(game.tcn, str)
        assert isinstance(game.uuid, str)
        assert isinstance(game.initial_setup, str)
        assert isinstance(game.fen, str)
        assert isinstance(game.time_class, str)
        assert isinstance(game.rules, str)
        assert isinstance(game.eco, str)
        assert isinstance(game.end_datetime, datetime)
        assert isinstance(game.start_datetime, (datetime, type(None)))

        assert isinstance(game.white.rating, int)
        assert isinstance(game.white.result, str)
        assert isinstance(game.white.username, str)
        assert isinstance(game.white.id, str)
        assert isinstance(game.white.uuid, str)

        assert isinstance(game.black.rating, int)
        assert isinstance(game.black.result, str)
        assert isinstance(game.black.username, str)
        assert isinstance(game.black.id, str)
        assert isinstance(game.black.uuid, str)