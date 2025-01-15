from unittest.mock import patch

import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_team_match_live.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_team_match_live(match_id=5833)
    validate_response(response)


@vcr.use_cassette("get_team_match_live.yaml")
def test_with_client(client):
    response = client.get_team_match_live(match_id=5833)
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_team_match_live.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_team_match_live(match_id=5833)
    validate_response(response)


@vcr.use_cassette("get_team_match_live.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_team_match_live(match_id=5833)

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)


def validate_response(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    assert response.json.get("match") is not None

    match = response.match
    assert isinstance(match.id, str)
    assert isinstance(match.name, str)
    assert isinstance(match.url, str)
    assert isinstance(match.start_time, int)
    assert isinstance(match.end_time, int)
    assert isinstance(match.status, str)
    assert isinstance(match.boards, int)
    assert isinstance(match.settings.rules, str)
    assert isinstance(match.settings.time_class, str)
    assert isinstance(match.settings.time_control, int)
    assert isinstance(match.settings.time_increment, int)
    assert isinstance(match.settings.min_team_players, int)
    assert isinstance(match.settings.min_required_games, int)
    assert isinstance(match.settings.autostart, bool)

    def validate_team(team):
        assert isinstance(team.id, str)
        assert isinstance(team.name, str)
        assert isinstance(team.url, str)
        assert isinstance(team.score, int)
        assert isinstance(team.result, str)

        for player in team.players:
            assert isinstance(player.username, str)
            assert isinstance(player.stats, str)
            assert isinstance(player.status, str)
            assert isinstance(player.played_as_white, str)
            assert isinstance(player.played_as_black, str)
            assert isinstance(player.board, str)

        assert isinstance(team.fair_play_removals, list)

    validate_team(match.teams.team1)
    validate_team(match.teams.team2)
