from unittest.mock import patch

import pytest

from chessdotcom.endpoints.player_stats import PlayerStats
from tests.vcr import vcr


@vcr.use_cassette("get_player_stats.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_player_stats(username="fabianocaruana")
    validate_response(response)


@vcr.use_cassette("get_player_stats.yaml")
def test_with_client(client):
    response = client.get_player_stats(username="fabianocaruana")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_player_stats.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_player_stats(username="fabianocaruana")
    validate_response(response)


@vcr.use_cassette("get_player_stats.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_player_stats(username="fabianocaruana")

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)
    assert isinstance(response.stats, PlayerStats)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("stats") is not None

    stats = response.stats
    assert isinstance(stats.chess_rapid.last.rating, int)
    assert isinstance(stats.chess_rapid.last.date, int)
    assert isinstance(stats.chess_rapid.last.rd, int)
    assert isinstance(stats.chess_rapid.best.rating, int)
    assert isinstance(stats.chess_rapid.best.date, int)
    assert isinstance(stats.chess_rapid.best.game, str)
    assert isinstance(stats.chess_rapid.record.win, int)
    assert isinstance(stats.chess_rapid.record.loss, int)
    assert isinstance(stats.chess_rapid.record.draw, int)

    assert isinstance(stats.chess_bullet.last.rating, int)
    assert isinstance(stats.chess_bullet.last.date, int)
    assert isinstance(stats.chess_bullet.last.rd, int)
    assert isinstance(stats.chess_bullet.best.rating, int)
    assert isinstance(stats.chess_bullet.best.date, int)
    assert isinstance(stats.chess_bullet.best.game, str)
    assert isinstance(stats.chess_bullet.record.win, int)
    assert isinstance(stats.chess_bullet.record.loss, int)
    assert isinstance(stats.chess_bullet.record.draw, int)

    assert isinstance(stats.chess_blitz.last.rating, int)
    assert isinstance(stats.chess_blitz.last.date, int)
    assert isinstance(stats.chess_blitz.last.rd, int)
    assert isinstance(stats.chess_blitz.best.rating, int)
    assert isinstance(stats.chess_blitz.best.date, int)
    assert isinstance(stats.chess_blitz.best.game, str)
    assert isinstance(stats.chess_blitz.record.win, int)
    assert isinstance(stats.chess_blitz.record.loss, int)
    assert isinstance(stats.chess_blitz.record.draw, int)

    assert isinstance(stats.fide, int)
    assert isinstance(stats.tactics.highest.rating, int)
    assert isinstance(stats.tactics.highest.date, int)
    assert isinstance(stats.tactics.lowest.rating, int)
    assert isinstance(stats.tactics.lowest.date, int)
    assert isinstance(stats.puzzle_rush.best.total_attempts, int)
    assert isinstance(stats.puzzle_rush.best.score, int)
