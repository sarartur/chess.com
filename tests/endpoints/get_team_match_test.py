import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_team_match.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_team_match(match_id=12803)
    validate_response(response)


@vcr.use_cassette("get_team_match.yaml")
def test_with_client(client):
    response = client.get_team_match(match_id=12803)
    validate_response(response)


@pytest.mark.asyncio
async def test_with_async_client(async_client):
    with vcr.use_cassette("get_team_match.yaml"):
        response = await async_client.get_team_match(match_id=12803)

    validate_response(response)


def validate_response(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    match = response.match

    assert isinstance(match.name, str)
    assert isinstance(match.url, str)
    assert isinstance(match.id, str)
    assert isinstance(match.status, str)
    assert isinstance(match.start_time, int)
    assert isinstance(match.end_time, int)
    assert isinstance(match.boards, int)

    assert isinstance(match.settings.rules, str)
    assert isinstance(match.settings.time_class, str)
    assert isinstance(match.settings.time_control, str)
    assert isinstance(match.settings.min_team_players, int)
    assert isinstance(match.settings.min_required_games, int)
    assert isinstance(match.settings.autostart, bool)

    def validate_team(team):
        assert isinstance(team.id, str)
        assert isinstance(team.name, str)
        assert isinstance(team.url, str)
        assert isinstance(team.score, float)
        assert isinstance(team.result, str)

        for player in team.players:
            assert isinstance(player.username, str)
            assert isinstance(player.stats, str)
            assert isinstance(player.status, str)
            assert isinstance(player.played_as_black, str)
            assert isinstance(player.board, str)

    validate_team(match.teams.team1)
    validate_team(match.teams.team2)
