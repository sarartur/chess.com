from datetime import datetime
from unittest.mock import patch

import pytest

from chessdotcom.endpoints.team_match import TeamMatch
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
@vcr.use_cassette("get_team_match.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_team_match(match_id=12803)
    validate_response(response)


@vcr.use_cassette("get_team_match.yaml")
@patch("chessdotcom.response_builder.Serializer.deserialize")
def test_empty_data(deserialize, client):
    deserialize.return_value = {}
    response = client.get_team_match(match_id=12803)

    validate_response_structure(response)


def validate_response_structure(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)
    assert isinstance(response.match, TeamMatch)


def validate_response(response):
    validate_response_structure(response)

    assert response.json.get("match") is not None

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

    assert isinstance(match.start_datetime, datetime)
    assert isinstance(match.end_datetime, datetime)

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
            assert isinstance(player.played_as_white, (str, type(None)))
            assert isinstance(player.board, str)
            assert isinstance(player.rating, (int, type(None)))
            assert isinstance(player.timeout_percent, (float, type(None)))

    validate_team(match.teams.team1)
    validate_team(match.teams.team2)
