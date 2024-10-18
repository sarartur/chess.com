import pytest

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
async def test_with_async_client(async_client):
    with vcr.use_cassette("get_club_members.yaml"):
        response = await async_client.get_club_members(
            url_id="chess-com-developer-community"
        )

    validate_response(response)


def validate_response(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    members = response.members
    for member in members.weekly:
        assert isinstance(member.username, str)
        assert isinstance(member.joined, int)

    for member in members.monthly:
        assert isinstance(member.username, str)
        assert isinstance(member.joined, int)

    for member in members.all_time:
        assert isinstance(member.username, str)
        assert isinstance(member.joined, int)
