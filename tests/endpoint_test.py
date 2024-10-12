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


@vcr.use_cassette("get_player_game_archives.yaml")
def test_get_player_game_archives():
    response = endpoints.get_player_game_archives("afgano29")

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    archives = response.archives
    assert all(isinstance(url, str) for url in archives)


@vcr.use_cassette("get_player_games_by_month.yaml")
def test_get_player_games_by_month():
    response = endpoints.get_player_games_by_month(
        username="fabianocaruana", year="2020", month="05"
    )

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    games = response.games
    for game in games:
        assert isinstance(game.url, str)
        assert isinstance(game.pgn, str)
        assert isinstance(game.time_control, str)
        assert isinstance(game.end_time, int)
        assert isinstance(game.accuracies.white, float)
        assert isinstance(game.accuracies.black, float)
        assert isinstance(game.tcn, str)
        assert isinstance(game.uuid, str)
        assert isinstance(game.initial_setup, str)
        assert isinstance(game.fen, str)
        assert isinstance(game.time_class, str)
        assert isinstance(game.rules, str)
        assert isinstance(game.eco, str)

        assert isinstance(game.white.rating, int)
        assert isinstance(game.white.result, str)
        assert isinstance(game.white.username, str)
        assert isinstance(game.white.id, str)
        assert isinstance(game.white.uuid, str)

        assert isinstance(game.black.rating, int)
        assert isinstance(game.black.result, str)
        assert isinstance(game.black.username, str)
        assert isinstance(game.black.id, str)
        assert isinstance(game.black.uuid, str)


@vcr.use_cassette("get_player_games_by_month_pgn.yaml")
def test_get_player_games_by_month_pgn():
    response = endpoints.get_player_games_by_month_pgn(
        username="fabianocaruana", year="2020", month="05"
    )

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    assert isinstance(response.pgn.pgn, str)


@vcr.use_cassette("get_player_clubs.yaml")
def test_get_player_clubs():
    response = endpoints.get_player_clubs(username="fabianocaruana")

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    for club in response.clubs:
        assert isinstance(club.id, str)
        assert isinstance(club.name, str)
        assert isinstance(club.last_activity, int)
        assert isinstance(club.icon, str)
        assert isinstance(club.url, str)
        assert isinstance(club.joined, int)


@vcr.use_cassette("get_player_team_matches.yaml")
def test_get_player_team_matches():
    response = endpoints.get_player_team_matches(username="akshayraj_kore")

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    def validate_match(match):
        assert isinstance(match.name, str)
        assert isinstance(match.url, str)
        assert isinstance(match.id, str)
        assert isinstance(match.club, str)
        assert isinstance(match.results.played_as_white, str)
        assert isinstance(match.results.played_as_black, str)
        assert isinstance(match.board, str)

    matches = response.matches
    for match in matches.finished:
        validate_match(match)

    for match in matches.in_progress:
        validate_match(match)

    for match in matches.registered:
        validate_match(match)


@vcr.use_cassette("get_player_tournaments.yaml")
def test_get_player_tournaments():
    response = endpoints.get_player_tournaments(username="fabianocaruana")

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    tournaments = response.tournaments
    for tournament in tournaments.finished:
        assert isinstance(tournament.url, str)
        assert isinstance(tournament.id, str)
        assert isinstance(tournament.wins, int)
        assert isinstance(tournament.losses, int)
        assert isinstance(tournament.draws, int)
        assert isinstance(tournament.placement, int)
        assert isinstance(tournament.status, str)
        assert isinstance(tournament.total_players, int)
        assert isinstance(tournament.time_class, str)
        assert isinstance(tournament.type, str)

    for tournament in tournaments.in_progress:
        assert isinstance(tournament.url, str)
        assert isinstance(tournament.id, str)
        assert isinstance(tournament.wins, int)
        assert isinstance(tournament.losses, int)
        assert isinstance(tournament.draws, int)
        assert isinstance(tournament.placement, int)
        assert isinstance(tournament.status, str)
        assert isinstance(tournament.total_players, int)
        assert isinstance(tournament.time_class, str)
        assert isinstance(tournament.type, str)

    for tournament in tournaments.registered:
        assert isinstance(tournament.url, str)
        assert isinstance(tournament.id, str)
        assert isinstance(tournament.status, str)
