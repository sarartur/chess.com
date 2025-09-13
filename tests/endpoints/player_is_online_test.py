from unittest.mock import patch

import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_player_is_online.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_player_is_online(username="erik")
    validate_response(response)


@vcr.use_cassette("get_player_is_online.yaml")
def test_with_client(client):
    response = client.get_player_is_online(username="erik")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_player_is_online.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_player_is_online(username="erik")
    validate_response(response)


@vcr.use_cassette("get_player_is_online.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_player_is_online(username="erik")

    validate_response_structure(response)


@vcr.use_cassette("get_player_is_online.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_online_true(deserialize, client):
    deserialize.return_value = {"online": True}
    response = client.get_player_is_online(username="erik")

    validate_response_structure(response)
    assert response.online is True


@vcr.use_cassette("get_player_is_online.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_online_false(deserialize, client):
    deserialize.return_value = {"online": False}
    response = client.get_player_is_online(username="erik")

    validate_response_structure(response)
    assert response.online is False


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)
    assert isinstance(response.online, (bool, type(None)))


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("online") is not None
    assert isinstance(response.online, bool)