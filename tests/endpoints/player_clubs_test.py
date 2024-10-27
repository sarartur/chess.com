from unittest.mock import patch

import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_player_clubs.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_player_clubs(username="fabianocaruana")
    validate_response(response)


@vcr.use_cassette("get_player_clubs.yaml")
def test_with_client(client):
    response = client.get_player_clubs(username="fabianocaruana")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_player_clubs.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_player_clubs(username="fabianocaruana")
    validate_response(response)


@vcr.use_cassette("get_player_clubs.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_player_clubs(username="fabianocaruana")

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)
    assert isinstance(response.clubs, list)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("clubs") is not None

    assert len(response.clubs) > 1
    for club in response.clubs:
        assert isinstance(club.id, str)
        assert isinstance(club.name, str)
        assert isinstance(club.last_activity, int)
        assert isinstance(club.icon, str)
        assert isinstance(club.url, str)
        assert isinstance(club.joined, int)
