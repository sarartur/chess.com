from datetime import datetime
from unittest.mock import patch

import pytest

from chessdotcom.endpoints.player_stats import PlayerStats
from tests.vcr import vcr


@vcr.use_cassette("get_player_stats.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_player_stats(username="erik")
    validate_response(response)


@vcr.use_cassette("get_player_stats.yaml")
def test_with_client(client):
    response = client.get_player_stats(username="erik")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_player_stats.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_player_stats(username="erik")
    validate_response(response)


@vcr.use_cassette("get_player_stats.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_player_stats(username="erik")

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)
    assert isinstance(response.stats, PlayerStats)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("stats") is not None

    stats = response.stats

    def validate_game_stats(game_stats):
        assert isinstance(game_stats.last.rating, int)
        assert isinstance(game_stats.last.date, int)
        assert isinstance(game_stats.last.datetime, datetime)
        assert isinstance(game_stats.last.rd, int)
        assert isinstance(game_stats.best.rating, int)
        assert isinstance(game_stats.best.date, int)
        assert isinstance(game_stats.best.datetime, datetime)
        assert isinstance(game_stats.best.game, str)
        assert isinstance(game_stats.record.win, int)
        assert isinstance(game_stats.record.loss, int)
        assert isinstance(game_stats.record.draw, int)

        if game_stats.tournament:
            assert isinstance(game_stats.tournament.count, int)
            assert isinstance(game_stats.tournament.withdraw, int)
            assert isinstance(game_stats.tournament.points, int)
            assert isinstance(game_stats.tournament.highest_finish, int)

    validate_game_stats(stats.chess_rapid)
    validate_game_stats(stats.chess_bullet)
    validate_game_stats(stats.chess_blitz)
    validate_game_stats(stats.chess_daily)
    validate_game_stats(stats.chess960_daily)

    assert isinstance(stats.fide, int)
    assert isinstance(stats.tactics.highest.rating, int)
    assert isinstance(stats.tactics.highest.date, int)
    assert isinstance(stats.tactics.highest.datetime, datetime)
    assert isinstance(stats.tactics.lowest.rating, int)
    assert isinstance(stats.tactics.lowest.date, int)
    assert isinstance(stats.tactics.lowest.datetime, datetime)
    assert isinstance(stats.puzzle_rush.best.total_attempts, int)
    assert isinstance(stats.puzzle_rush.best.score, int)
