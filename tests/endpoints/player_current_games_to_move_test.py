from datetime import datetime
from unittest.mock import patch

import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_player_current_games_to_move.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_player_current_games_to_move(username="plutopete")
    validate_response(response)


@vcr.use_cassette("get_player_current_games_to_move.yaml")
def test_with_client(client):
    response = client.get_player_current_games_to_move(username="plutopete")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_player_current_games_to_move.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_player_current_games_to_move(username="plutopete")
    validate_response(response)


@vcr.use_cassette("get_player_current_games_to_move.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_player_current_games_to_move(username="plutopete")

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("games") is not None

    games = response.games
    assert len(games) > 0

    for game in games:
        assert isinstance(game.url, str)
        assert isinstance(game.move_by, int)
        assert isinstance(game.last_activity, int)
        assert isinstance(game.draw_offer, (bool, type(None)))
        assert isinstance(game.move_by_datetime, datetime)
        assert isinstance(game.last_activity_datetime, datetime)
