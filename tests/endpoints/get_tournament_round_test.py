import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_tournament_round.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_tournament_round(
        url_id="-33rd-chesscom-quick-knockouts-1401-1600", round_num=1
    )
    validate_response(response)


@vcr.use_cassette("get_tournament_round.yaml")
def test_with_client(client):
    response = client.get_tournament_round(
        url_id="-33rd-chesscom-quick-knockouts-1401-1600", round_num=1
    )
    validate_response(response)


@pytest.mark.asyncio
async def test_with_async_client(async_client):
    with vcr.use_cassette("get_tournament_round.yaml"):
        response = await async_client.get_tournament_round(
            url_id="-33rd-chesscom-quick-knockouts-1401-1600", round_num=1
        )

    validate_response(response)


def validate_response(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    round = response.tournament_round

    groups = round.groups
    assert all(isinstance(group, str) for group in groups)

    for player in round.players:
        assert isinstance(player.username, str)
        assert isinstance(player.is_advancing, bool)
