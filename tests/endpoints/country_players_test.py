from unittest.mock import patch

import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_country_players.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_country_players(iso="US")
    validate_response(response)


@vcr.use_cassette("get_country_players.yaml")
def test_with_client(client):
    response = client.get_country_players(iso="US")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_country_players.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_country_players(iso="US")
    validate_response(response)


@vcr.use_cassette("get_country_players.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_country_players(iso="US")

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)
    assert isinstance(response.players, list)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("players") is not None

    assert all(isinstance(player, str) for player in response.players)
