from unittest.mock import patch

import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_leaderboards.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_leaderboards()
    validate_response(response)


@vcr.use_cassette("get_leaderboards.yaml")
def test_with_client(client):
    response = client.get_leaderboards()
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_leaderboards.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_leaderboards()
    validate_response(response)


@vcr.use_cassette("get_leaderboards.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_leaderboards()

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("leaderboards") is not None

    def validate_leaderboard(leaderboard):
        for player in leaderboard:
            assert isinstance(player.player_id, int)
            assert isinstance(player.id, str)
            assert isinstance(player.url, str)
            assert isinstance(player.username, str)
            assert isinstance(player.score, int)
            assert isinstance(player.rank, int)
            assert isinstance(player.country, str)
            # assert isinstance(player.title, str)
            # assert isinstance(player.name, str)
            assert isinstance(player.status, str)
            assert isinstance(player.avatar, str)
            # assert isinstance(player.trend_score.direction, int)
            # assert isinstance(player.trend_score.delta, int)
            # assert isinstance(player.trend_rank.direction, int)
            # assert isinstance(player.trend_rank.delta, int)
            assert isinstance(player.flair_code, str)
            assert isinstance(player.win_count, int)
            assert isinstance(player.loss_count, int)
            assert isinstance(player.draw_count, int)

    leaderboards = response.leaderboards
    validate_leaderboard(leaderboards.daily)
    validate_leaderboard(leaderboards.daily960)
    validate_leaderboard(leaderboards.live_rapid)
    validate_leaderboard(leaderboards.live_blitz)
    validate_leaderboard(leaderboards.live_bullet)
    validate_leaderboard(leaderboards.live_bughouse)
    validate_leaderboard(leaderboards.live_blitz960)
    validate_leaderboard(leaderboards.live_threecheck)
    validate_leaderboard(leaderboards.live_crazyhouse)
    validate_leaderboard(leaderboards.live_kingofthehill)
    validate_leaderboard(leaderboards.tactics)
    validate_leaderboard(leaderboards.rush)
    validate_leaderboard(leaderboards.battle)
