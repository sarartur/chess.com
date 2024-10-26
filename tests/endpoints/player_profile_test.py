import datetime
from unittest.mock import patch

import pytest

from chessdotcom.endpoints.player_profile import PlayerProfile
from tests.vcr import vcr


@vcr.use_cassette("get_player_profile.yaml")
def test_get_with_endpoints(endpoints):
    response = endpoints.get_player_profile(username="farzyplayschess")
    validate_response(response)


@vcr.use_cassette("get_player_profile.yaml")
def test_get_with_client(client):
    response = client.get_player_profile(username="farzyplayschess")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_player_profile.yaml")
async def test_get_with_async_client(async_client):
    response = await async_client.get_player_profile(username="farzyplayschess")
    validate_response(response)


@vcr.use_cassette("get_player_profile.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_player_profile(username="farzyplayschess")

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)
    assert isinstance(response.player, PlayerProfile)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("player") is not None

    player = response.player
    assert isinstance(player.avatar, str)
    assert isinstance(player.player_id, int)
    assert isinstance(player.id, str)
    assert isinstance(player.url, str)
    assert isinstance(player.name, (str, type(None)))
    assert isinstance(player.username, str)
    assert isinstance(player.title, (str, type(None)))
    assert isinstance(player.followers, int)
    assert isinstance(player.country, str)
    assert isinstance(player.last_online, int)
    assert isinstance(player.joined, int)
    assert isinstance(player.status, str)
    assert isinstance(player.is_streamer, bool)
    assert isinstance(player.verified, bool)
    assert isinstance(player.league, str)

    assert isinstance(player.last_online_datetime, datetime.datetime)
    assert isinstance(player.joined_datetime, datetime.datetime)

    def validate_streaming_platform(platform):
        assert isinstance(platform.type, str)
        assert isinstance(platform.channel_url, str)

    for platform in player.streaming_platforms:
        validate_streaming_platform(platform)
