import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_club_matches.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_club_matches(url_id="chess-com-developer-community")
    validate_response(response)


@vcr.use_cassette("get_club_matches.yaml")
def test_with_client(client):
    response = client.get_club_matches(url_id="chess-com-developer-community")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_club_matches.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_club_matches(
        url_id="chess-com-developer-community"
    )
    validate_response(response)


def validate_response(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    matches = response.matches
    for match in matches.finished:
        assert isinstance(match.name, str)
        assert isinstance(match.id, str)
        assert isinstance(match.opponent, str)
        assert isinstance(match.start_time, int)
        assert isinstance(match.time_class, str)
        assert isinstance(match.result, str)

    for match in matches.in_progress:
        assert isinstance(match.name, str)
        assert isinstance(match.id, str)
        assert isinstance(match.opponent, str)
        assert isinstance(match.start_time, int)
        assert isinstance(match.time_class, str)

    for match in matches.registered:
        assert isinstance(match.name, str)
        assert isinstance(match.id, str)
        assert isinstance(match.opponent, str)
        assert isinstance(match.time_class, str)
