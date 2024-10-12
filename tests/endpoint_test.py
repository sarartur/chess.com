from chessdotcom import endpoints
from tests.vcr import vcr


@vcr.use_cassette("get_player_profile.yaml")
def test_get_player_profile():
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

    matches = response.matches
    for match in matches.finished:
        assert isinstance(match.name, str)
        assert isinstance(match.url, str)
        assert isinstance(match.id, str)
        assert isinstance(match.club, str)
        assert isinstance(match.results.played_as_white, str)
        assert isinstance(match.results.played_as_black, str)
        assert isinstance(match.board, str)

    for match in matches.in_progress:
        assert isinstance(match.name, str)
        assert isinstance(match.url, str)
        assert isinstance(match.id, str)
        assert isinstance(match.club, str)
        assert isinstance(match.board, str)

    for match in matches.registered:
        assert isinstance(match.name, str)
        assert isinstance(match.url, str)
        assert isinstance(match.id, str)
        assert isinstance(match.club, str)


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
        assert isinstance(tournament.status, str)

    for tournament in tournaments.registered:
        assert isinstance(tournament.url, str)
        assert isinstance(tournament.id, str)
        assert isinstance(tournament.status, str)


@vcr.use_cassette("get_club_details.yaml")
def test_get_club_details():
    response = endpoints.get_club_details("chess-com-developer-community")

    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    club = response.club
    assert isinstance(club.name, str)
    assert isinstance(club.url, str)
    assert isinstance(club.icon, str)
    assert isinstance(club.country, str)
    assert isinstance(club.id, str)
    assert isinstance(club.club_id, int)
    assert isinstance(club.average_daily_rating, int)
    assert isinstance(club.members_count, int)
    assert isinstance(club.created, int)
    assert isinstance(club.last_activity, int)
    assert all(isinstance(a, str) for a in club.admin)
    assert isinstance(club.visibility, str)
    assert isinstance(club.join_request, str)
    assert isinstance(club.description, str)


@vcr.use_cassette("get_club_members.yaml")
def test_get_club_members():
    response = endpoints.get_club_members("chess-com-developer-community")

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


@vcr.use_cassette("get_club_matches.yaml")
def test_get_club_matches():
    response = endpoints.get_club_matches("chess-com-developer-community")

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
