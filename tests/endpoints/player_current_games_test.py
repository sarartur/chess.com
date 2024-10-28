import pytest

from tests.vcr import vcr


@vcr.use_cassette("get_player_current_games.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_player_current_games(username="afgano29")
    validate_response(response)


@vcr.use_cassette("get_player_current_games.yaml")
def test_with_client(client):
    response = client.get_player_current_games(username="afgano29")
    validate_response(response)


@pytest.mark.asyncio
@vcr.use_cassette("get_player_current_games.yaml")
async def test_with_async_client(async_client):
    response = await async_client.get_player_current_games(username="afgano29")
    validate_response(response)


def validate_response(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    games = response.games
    for game in games:
        assert isinstance(game.url, str)
        assert isinstance(game.move_by, int)
        assert isinstance(game.pgn, str)
        assert isinstance(game.time_control, str)
        assert isinstance(game.start_time, int)
        assert isinstance(game.last_activity, int)
        assert isinstance(game.rated, bool)
        assert isinstance(game.turn, str)
        assert isinstance(game.fen, str)
        assert isinstance(game.time_class, str)
        assert isinstance(game.rules, str)
        assert isinstance(game.white, str)
        assert isinstance(game.black, str)
