from unittest.mock import patch

import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_tournament_round.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_tournament_round(
        url_id="-33rd-chesscom-quick-knockouts-1401-1600", round_num=1
    )
    validate_response(response)


@vcr.use_cassette("get_tournament_round.yaml")
def test_with_client(client):
    response = client.get_tournament_round(
        url_id="-33rd-chesscom-quick-knockouts-1401-1600", round_num=1
    )
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_tournament_round.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_tournament_round(
        url_id="-33rd-chesscom-quick-knockouts-1401-1600", round_num=1
    )
    validate_response(response)


@vcr.use_cassette("get_tournament_round.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_tournament_round(
        url_id="-33rd-chesscom-quick-knockouts-1401-1600", round_num=1
    )

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("tournament_round") is not None

    round = response.tournament_round

    groups = round.groups
    assert all(isinstance(group, str) for group in groups)

    for player in round.players:
        assert isinstance(player.username, str)
        assert isinstance(player.is_advancing, bool)
