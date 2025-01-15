from unittest.mock import patch

import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_team_match_live_board.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_team_match_live_board(match_id=5833, board_num=1)
    validate_response(response)


@vcr.use_cassette("get_team_match_live_board.yaml")
def test_with_client(client):
    response = client.get_team_match_live_board(match_id=5833, board_num=1)
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_team_match_live_board.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_team_match_live_board(match_id=5833, board_num=1)
    validate_response(response)


@vcr.use_cassette("get_team_match_live_board.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_team_match_live_board(match_id=5833, board_num=1)

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)


def validate_response(response):
    validate_response_structure(response)

    match_board = response.match_board

    # board_scores = match_board.board_scores
    # assert isinstance(board_scores, dict)

    games = match_board.games
    assert len(games) > 1
    for game in games:
        assert isinstance(game.url, str)
        assert isinstance(game.pgn, str)
        assert isinstance(game.time_control, str)
        assert isinstance(game.end_time, int)
        assert isinstance(game.rated, bool)
        assert isinstance(game.fen, str)
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
        assert isinstance(game.eco, str)
