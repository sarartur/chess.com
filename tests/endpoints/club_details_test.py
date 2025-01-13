from datetime import datetime
from unittest.mock import patch

import pytest

from chessdotcom.endpoints.club_details import ClubDetails
from tests.vcr import vcr


@vcr.use_cassette("get_club_details.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_club_details(url_id="chess-com-developer-community")
    validate_response(response)


@vcr.use_cassette("get_club_details.yaml")
def test_with_client(client):
    response = client.get_club_details(url_id="chess-com-developer-community")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_club_details.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_club_details(
        url_id="chess-com-developer-community"
    )
    validate_response(response)


@vcr.use_cassette("get_club_details.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_club_details(url_id="chess-com-developer-community")

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)
    assert isinstance(response.club, ClubDetails)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("club") is not None

    club = response.club
    assert isinstance(club.name, str)
    assert isinstance(club.url, str)
    assert isinstance(club.icon, str)
    assert isinstance(club.country, str)
    assert isinstance(club.id, str)
    assert isinstance(club.club_id, int)
    assert isinstance(club.average_daily_rating, int)
    assert isinstance(club.members_count, int)
    assert isinstance(club.created, int)
    assert isinstance(club.last_activity, int)
    assert all(isinstance(a, str) for a in club.admin)
    assert isinstance(club.visibility, str)
    assert isinstance(club.join_request, str)
    assert isinstance(club.description, str)
    assert isinstance(club.last_activity_datetime, datetime)
    assert isinstance(club.created_datetime, datetime)
