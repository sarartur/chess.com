from chessdotcom import endpoints
from tests.vcr import vcr


@vcr.use_cassette("get_tournament_details.yaml")
def test_get_tournament_details():
    response = endpoints.get_tournament_details(
        "-33rd-chesscom-quick-knockouts-1401-1600"
    )

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    tournament = response.tournament

    assert isinstance(tournament.name, str)
    assert isinstance(tournament.url, str)
    assert isinstance(tournament.description, str)
    assert isinstance(tournament.creator, str)
    assert isinstance(tournament.status, str)
    assert isinstance(tournament.finish_time, int)
    assert isinstance(tournament.settings.type, str)
    assert isinstance(tournament.settings.rules, str)
    assert isinstance(tournament.settings.is_rated, bool)
    assert isinstance(tournament.settings.is_official, bool)
    assert isinstance(tournament.settings.is_invite_only, bool)
    assert isinstance(tournament.settings.min_rating, int)
    assert isinstance(tournament.settings.max_rating, int)
    assert isinstance(tournament.settings.initial_group_size, int)
    assert isinstance(tournament.settings.user_advance_count, int)
    assert isinstance(tournament.settings.use_tiebreak, bool)
    assert isinstance(tournament.settings.allow_vacation, bool)
    assert isinstance(tournament.settings.winner_places, int)
    assert isinstance(tournament.settings.registered_user_count, int)
    assert isinstance(tournament.settings.games_per_opponent, int)
    assert isinstance(tournament.settings.total_rounds, int)
    assert isinstance(tournament.settings.concurrent_games_per_opponent, int)
    assert isinstance(tournament.settings.time_class, str)
    assert isinstance(tournament.settings.time_control, str)

    for player in tournament.players:
        assert isinstance(player.username, str)
        assert isinstance(player.status, str)

    assert all(isinstance(round, str) for round in tournament.rounds)


@vcr.use_cassette("get_tournament_round.yaml")
def test_get_tournament_round():
    response = endpoints.get_tournament_round(
        "-33rd-chesscom-quick-knockouts-1401-1600", 1
    )

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    round = response.tournament_round

    groups = round.groups
    assert all(isinstance(group, str) for group in groups)

    for player in round.players:
        assert isinstance(player.username, str)
        assert isinstance(player.is_advancing, bool)


@vcr.use_cassette("get_tournament_round_group_details(.yaml")
def test_get_tournament_round_group_details():
    response = endpoints.get_tournament_round_group_details(
        "-33rd-chesscom-quick-knockouts-1401-1600", 1, 1
    )

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    tournament_round_group = response.tournament_round_group
    assert isinstance(tournament_round_group.fair_play_removals, list)

    for player in tournament_round_group.players:
        assert isinstance(player.username, str)
        assert isinstance(player.points, (float, int))
        assert isinstance(player.is_advancing, bool)
        assert isinstance(player.tie_break, (float, int))

    for game in tournament_round_group.games:
        assert isinstance(game.url, str)
        assert isinstance(game.pgn, str)
        assert isinstance(game.time_control, str)
        assert isinstance(game.end_time, int)
        assert isinstance(game.rated, bool)
        assert isinstance(game.fen, str)
        assert isinstance(game.start_time, int)
        assert isinstance(game.time_class, str)
        assert isinstance(game.rules, str)

        assert isinstance(game.white.rating, int)
        assert isinstance(game.white.result, str)
        assert isinstance(game.white.id, str)
        assert isinstance(game.white.username, str)
        assert isinstance(game.white.uuid, str)

        assert isinstance(game.black.rating, int)
        assert isinstance(game.black.result, str)
        assert isinstance(game.black.id, str)
        assert isinstance(game.black.username, str)
        assert isinstance(game.black.uuid, str)


@vcr.use_cassette("get_team_match.yaml")
def test_get_team_match():
    response = endpoints.get_team_match(12803)

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


@vcr.use_cassette("get_team_match_board.yaml")
def test_get_team_match_board():
    response = endpoints.get_team_match_board(12803, 1)

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    match_board = response.match_board
    # assert isinstance(match_board.board_scores, dict)

    games = match_board.games
    for game in games:
        assert isinstance(game.url, str)
        assert isinstance(game.pgn, str)
        assert isinstance(game.time_control, str)
        assert isinstance(game.end_time, int)
        assert isinstance(game.rated, bool)
        assert isinstance(game.fen, str)
        assert isinstance(game.start_time, int)
        assert isinstance(game.time_class, str)
        assert isinstance(game.rules, str)
        assert isinstance(game.white.rating, int)
        assert isinstance(game.white.result, str)
        assert isinstance(game.white.id, str)
        assert isinstance(game.white.username, str)
        assert isinstance(game.white.uuid, str)
        assert isinstance(game.black.rating, int)
        assert isinstance(game.black.result, str)
        assert isinstance(game.black.id, str)
        assert isinstance(game.black.username, str)
        assert isinstance(game.black.uuid, str)
        assert isinstance(game.match, str)


@vcr.use_cassette("get_team_match_live.yaml")
def test_get_team_match_live():
    response = endpoints.get_team_match_live(5833)

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

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


@vcr.use_cassette("get_team_match_live_board.yaml")
def test_get_team_match_live_board():
    response = endpoints.get_team_match_live(5833, 1)

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

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


@vcr.use_cassette("get_country_details.yaml")
def test_get_country_details():
    response = endpoints.get_country_details("XE")

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    country = response.country
    assert isinstance(country.name, str)
    assert isinstance(country.id, str)
    assert isinstance(country.code, str)


@vcr.use_cassette("get_country_players.yaml")
def test_get_country_players():
    response = endpoints.get_country_players("US")

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    assert all(isinstance(player, str) for player in response.players)


@vcr.use_cassette("get_country_clubs.yaml")
def test_get_country_clubs():
    response = endpoints.get_country_clubs("XE")

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    assert all(isinstance(club, str) for club in response.clubs)


@vcr.use_cassette("get_current_daily_puzzle.yaml")
def test_get_current_daily_puzzle():
    response = endpoints.get_current_daily_puzzle()

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    puzzle = response.puzzle

    assert isinstance(puzzle.title, str)
    assert isinstance(puzzle.url, str)
    assert isinstance(puzzle.publish_time, int)
    assert isinstance(puzzle.fen, str)
    assert isinstance(puzzle.pgn, str)
    assert isinstance(puzzle.image, str)


@vcr.use_cassette("get_random_daily_puzzle.yaml")
def test_get_random_daily_puzzle():
    response = endpoints.get_current_daily_puzzle()

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    puzzle = response.puzzle

    assert isinstance(puzzle.title, str)
    assert isinstance(puzzle.url, str)
    assert isinstance(puzzle.publish_time, int)
    assert isinstance(puzzle.fen, str)
    assert isinstance(puzzle.pgn, str)
    assert isinstance(puzzle.image, str)


@vcr.use_cassette("get_streamers.yaml")
def test_get_streamers():
    response = endpoints.get_streamers()

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    streamers = response.streamers

    for streamer in streamers:
        assert isinstance(streamer.username, str)
        assert isinstance(streamer.avatar, str)
        # assert isinstance(streamer.twitch_url, str)
        assert isinstance(streamer.url, str)
        assert isinstance(streamer.is_live, bool)
        assert isinstance(streamer.is_community_streamer, bool)

        for platform in streamer.platforms:
            assert isinstance(platform.type, str)
            # assert isinstance(platform.stream_url, str)
            assert isinstance(platform.channel_url, str)
            assert isinstance(platform.is_live, bool)
            # assert isinstance(platform.is_main_live_platform, bool)


@vcr.use_cassette("get_leaderboards.yaml")
def test_get_leaderboards():
    response = endpoints.get_leaderboards()

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    def validate_leaderboard(leaderboard):
        for player in leaderboard:
            assert isinstance(player.player_id, int)
            assert isinstance(player.id, str)
            assert isinstance(player.url, str)
            assert isinstance(player.username, str)
            assert isinstance(player.score, int)
            assert isinstance(player.rank, int)
            assert isinstance(player.country, str)
            # assert isinstance(player.title, str)
            # assert isinstance(player.name, str)
            assert isinstance(player.status, str)
            assert isinstance(player.avatar, str)
            # assert isinstance(player.trend_score.direction, int)
            # assert isinstance(player.trend_score.delta, int)
            # assert isinstance(player.trend_rank.direction, int)
            # assert isinstance(player.trend_rank.delta, int)
            assert isinstance(player.flair_code, str)
            assert isinstance(player.win_count, int)
            assert isinstance(player.loss_count, int)
            assert isinstance(player.draw_count, int)

    leaderboards = response.leaderboards
    validate_leaderboard(leaderboards.daily)
    validate_leaderboard(leaderboards.daily960)
    validate_leaderboard(leaderboards.live_rapid)
    validate_leaderboard(leaderboards.live_blitz)
    validate_leaderboard(leaderboards.live_bullet)
    validate_leaderboard(leaderboards.live_bughouse)
    validate_leaderboard(leaderboards.live_blitz960)
    validate_leaderboard(leaderboards.live_threecheck)
    validate_leaderboard(leaderboards.live_crazyhouse)
    validate_leaderboard(leaderboards.live_kingofthehill)
    validate_leaderboard(leaderboards.tactics)
    validate_leaderboard(leaderboards.rush)
    validate_leaderboard(leaderboards.battle)
