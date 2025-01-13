from datetime import datetime
from unittest.mock import patch

import pytest

from chessdotcom.endpoints.club_members import ClubMembers
from tests.vcr import vcr


@vcr.use_cassette("get_club_members.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_club_members(url_id="chess-com-developer-community")
    validate_response(response)


@vcr.use_cassette("get_club_members.yaml")
def test_with_client(client):
    response = client.get_club_members(url_id="chess-com-developer-community")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_club_members.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_club_members(
        url_id="chess-com-developer-community"
    )
    validate_response(response)


@vcr.use_cassette("get_club_members.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_club_members(url_id="chess-com-developer-community")

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)
    assert isinstance(response.members, ClubMembers)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("members") is not None

    members = response.members

    validate_members(members.weekly)
    validate_members(members.monthly)
    validate_members(members.all_time)


def validate_members(members):
    for member in members:
        assert isinstance(member.username, str)
        assert isinstance(member.joined, int)
        assert isinstance(member.joined_datetime, datetime)
