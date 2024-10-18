import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_country_clubs.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_country_clubs(iso="XE")
    validate_response(response)


@vcr.use_cassette("get_country_clubs.yaml")
def test_with_client(client):
    response = client.get_country_clubs(iso="XE")
    validate_response(response)


@pytest.mark.asyncio
async def test_with_async_client(async_client):
    with vcr.use_cassette("get_country_clubs.yaml"):
        response = await async_client.get_country_clubs(iso="XE")

    validate_response(response)


def validate_response(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    assert all(isinstance(club, str) for club in response.clubs)
