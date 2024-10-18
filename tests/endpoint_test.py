from chessdotcom import endpoints
from tests.vcr import vcr


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
