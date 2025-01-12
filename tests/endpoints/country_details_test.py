from unittest.mock import patch

import pytest

from chessdotcom.endpoints.country_details import CountryDetails
from tests.vcr import vcr


@vcr.use_cassette("get_country_details.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_country_details(iso="XE")
    validate_response(response)


@vcr.use_cassette("get_country_details.yaml")
def test_with_client(client):
    response = client.get_country_details(iso="XE")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_country_details.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_country_details(iso="XE")
    validate_response(response)


@vcr.use_cassette("get_country_details.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_country_details(iso="XE")

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)
    assert isinstance(response.country, CountryDetails)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("country") is not None

    country = response.country
    assert isinstance(country.name, str)
    assert isinstance(country.id, str)
    assert isinstance(country.code, str)
