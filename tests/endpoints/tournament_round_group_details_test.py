from unittest.mock import patch

import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_tournament_round_group_details.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_tournament_round_group_details(
        url_id="-33rd-chesscom-quick-knockouts-1401-1600", round_num=1, group_num=1
    )
    validate_response(response)


@vcr.use_cassette("get_tournament_round_group_details.yaml")
def test_with_client(client):
    response = client.get_tournament_round_group_details(
        url_id="-33rd-chesscom-quick-knockouts-1401-1600", round_num=1, group_num=1
    )
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_tournament_round_group_details.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_tournament_round_group_details(
        url_id="-33rd-chesscom-quick-knockouts-1401-1600", round_num=1, group_num=1
    )
    validate_response(response)


@vcr.use_cassette("get_tournament_round_group_details.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_tournament_round_group_details(
        url_id="-33rd-chesscom-quick-knockouts-1401-1600", round_num=1, group_num=1
    )

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("tournament_round_group") is not None

    tournament_round_group = response.tournament_round_group
    assert isinstance(tournament_round_group.fair_play_removals, list)

    for player in tournament_round_group.players:
        assert isinstance(player.username, str)
        assert isinstance(player.points, (float, int))
        assert isinstance(player.is_advancing, bool)
        assert isinstance(player.tie_break, (float, int))

    for game in tournament_round_group.games:
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
