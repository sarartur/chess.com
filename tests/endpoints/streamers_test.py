from unittest.mock import patch

import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_streamers.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_streamers()
    validate_response(response)


@vcr.use_cassette("get_streamers.yaml")
def test_with_client(client):
    response = client.get_streamers()
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_streamers.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_streamers()
    validate_response(response)


@vcr.use_cassette("get_streamers.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_streamers()

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("streamers") is not None

    streamers = response.streamers

    for streamer in streamers:
        assert isinstance(streamer.username, str)
        assert isinstance(streamer.avatar, str)
        # assert isinstance(streamer.twitch_url, str)
        assert isinstance(streamer.url, str)
        assert isinstance(streamer.is_live, bool)
        assert isinstance(streamer.is_community_streamer, bool)

        for platform in streamer.platforms:
            assert isinstance(platform.type, str)
            # assert isinstance(platform.stream_url, str)
            assert isinstance(platform.channel_url, str)
            assert isinstance(platform.is_live, bool)
            # assert isinstance(platform.is_main_live_platform, bool)
