from unittest.mock import patch

import pytest

from chessdotcom.endpoints.random_daily_puzzle import Puzzle
from tests.vcr import vcr


@vcr.use_cassette("get_random_daily_puzzle.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_random_daily_puzzle()
    validate_response(response)


@vcr.use_cassette("get_random_daily_puzzle.yaml")
def test_with_client(client):
    response = client.get_random_daily_puzzle()
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_random_daily_puzzle.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_random_daily_puzzle()
    validate_response(response)


@vcr.use_cassette("get_random_daily_puzzle.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_random_daily_puzzle()

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)
    assert isinstance(response.puzzle, Puzzle)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("puzzle") is not None

    puzzle = response.puzzle

    assert isinstance(puzzle.title, str)
    assert isinstance(puzzle.url, str)
    assert isinstance(puzzle.publish_time, int)
    assert isinstance(puzzle.fen, str)
    assert isinstance(puzzle.pgn, str)
    assert isinstance(puzzle.image, str)
