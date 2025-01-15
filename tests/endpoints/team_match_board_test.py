from datetime import datetime
from unittest.mock import patch

import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_team_match_board.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_team_match_board(match_id=12803, board_num=1)
    validate_response(response)


@vcr.use_cassette("get_team_match_board.yaml")
def test_with_client(client):
    response = client.get_team_match_board(match_id=12803, board_num=1)
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_team_match_board.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_team_match_board(match_id=12803, board_num=1)
    validate_response(response)


@vcr.use_cassette("get_team_match_board.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_team_match_board(match_id=12803, board_num=1)

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)


def validate_response(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    assert response.json.get("match_board") is not None

    match_board = response.match_board
    assert isinstance(match_board.board_scores, dict)

    games = match_board.games
    for game in games:
        assert isinstance(game.url, str)
        assert isinstance(game.pgn, str)
        assert isinstance(game.time_control, str)
        assert isinstance(game.end_time, int)
        assert isinstance(game.rated, bool)
        assert isinstance(game.fen, str)
        assert isinstance(game.start_time, int)
        assert isinstance(game.time_class, str)
        assert isinstance(game.rules, str)
        assert isinstance(game.white.rating, int)
        assert isinstance(game.white.result, str)
        assert isinstance(game.white.id, str)
        assert isinstance(game.white.username, str)
        assert isinstance(game.white.uuid, str)
        assert isinstance(game.black.rating, int)
        assert isinstance(game.black.result, str)
        assert isinstance(game.black.id, str)
        assert isinstance(game.black.username, str)
        assert isinstance(game.black.uuid, str)
        assert isinstance(game.match, str)
        assert isinstance(game.end_datetime, datetime)
        assert isinstance(game.start_datetime, datetime)
