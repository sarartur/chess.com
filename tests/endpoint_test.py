from chessdotcom import endpoints
from tests.vcr import vcr


@vcr.use_cassette("get_player_profile.yaml")
def test_get_club_details():
    response = endpoints.get_player_profile("fabianocaruana")

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    player = response.player
    assert isinstance(player.avatar, str)
    assert isinstance(player.player_id, int)
    assert isinstance(player.id, str)
    assert isinstance(player.url, str)
    assert isinstance(player.name, str)
    assert isinstance(player.username, str)
    assert isinstance(player.title, str)
    assert isinstance(player.followers, int)
    assert isinstance(player.country, str)
    assert isinstance(player.last_online, int)
    assert isinstance(player.joined, int)
    assert isinstance(player.status, str)
    assert isinstance(player.is_streamer, bool)
    assert isinstance(player.verified, bool)
    assert isinstance(player.league, str)
    assert isinstance(player.streaming_platforms, list)


@vcr.use_cassette("get_titled_players.yaml")
def test_get_titled_players():
    response = endpoints.get_titled_players("GM")

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    players = response.players
    assert isinstance(players, list)
    assert all(isinstance(player, str) for player in players)


@vcr.use_cassette("get_player_stats.yaml")
def test_get_player_stats():
    response = endpoints.get_player_stats("fabianocaruana")

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    stats = response.stats
    assert isinstance(stats.chess_rapid.last.rating, int)
    assert isinstance(stats.chess_rapid.last.date, int)
    assert isinstance(stats.chess_rapid.last.rd, int)
    assert isinstance(stats.chess_rapid.best.rating, int)
    assert isinstance(stats.chess_rapid.best.date, int)
    assert isinstance(stats.chess_rapid.best.game, str)
    assert isinstance(stats.chess_rapid.record.win, int)
    assert isinstance(stats.chess_rapid.record.loss, int)
    assert isinstance(stats.chess_rapid.record.draw, int)

    assert isinstance(stats.chess_bullet.last.rating, int)
    assert isinstance(stats.chess_bullet.last.date, int)
    assert isinstance(stats.chess_bullet.last.rd, int)
    assert isinstance(stats.chess_bullet.best.rating, int)
    assert isinstance(stats.chess_bullet.best.date, int)
    assert isinstance(stats.chess_bullet.best.game, str)
    assert isinstance(stats.chess_bullet.record.win, int)
    assert isinstance(stats.chess_bullet.record.loss, int)
    assert isinstance(stats.chess_bullet.record.draw, int)

    assert isinstance(stats.chess_blitz.last.rating, int)
    assert isinstance(stats.chess_blitz.last.date, int)
    assert isinstance(stats.chess_blitz.last.rd, int)
    assert isinstance(stats.chess_blitz.best.rating, int)
    assert isinstance(stats.chess_blitz.best.date, int)
    assert isinstance(stats.chess_blitz.best.game, str)
    assert isinstance(stats.chess_blitz.record.win, int)
    assert isinstance(stats.chess_blitz.record.loss, int)
    assert isinstance(stats.chess_blitz.record.draw, int)

    assert isinstance(stats.fide, int)
    assert isinstance(stats.tactics.highest.rating, int)
    assert isinstance(stats.tactics.highest.date, int)
    assert isinstance(stats.tactics.lowest.rating, int)
    assert isinstance(stats.tactics.lowest.date, int)
    assert isinstance(stats.puzzle_rush.best.total_attempts, int)
    assert isinstance(stats.puzzle_rush.best.score, int)


@vcr.use_cassette("get_player_current_games.yaml")
def test_get_player_current_games():
    response = endpoints.get_player_current_games("afgano29")

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


@vcr.use_cassette("get_player_current_games_to_move.yaml")
def test_get_player_current_games_to_move():
    response = endpoints.get_player_current_games_to_move("afgano29")

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    games = response.games
    for game in games:
        assert isinstance(game.url, str)
        assert isinstance(game.move_by, int)
        assert isinstance(game.last_activity, int)
