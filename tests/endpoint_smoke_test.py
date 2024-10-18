import asyncio

from chessdotcom import ChessDotComResponse, endpoints
from chessdotcom.client import ChessDotComClient, RateLimitHandler


def test_endpoints():
    endpoints.Client.aio = False

    data = endpoints.get_player_profile("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_titled_players("GM")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_player_stats("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_player_current_games("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_player_current_games_to_move("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_player_game_archives("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_player_games_by_month(
        username="fabianocaruana", year="2020", month="05"
    )
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_player_games_by_month_pgn(
        username="fabianocaruana", year="2020", month="05"
    )
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_player_clubs("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_player_team_matches("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_player_tournaments("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_club_details("chess-com-developer-community")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_club_members("chess-com-developer-community")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_club_matches("chess-com-developer-community")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_tournament_details("-33rd-chesscom-quick-knockouts-1401-1600")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_tournament_round("-33rd-chesscom-quick-knockouts-1401-1600", 1)
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_tournament_round_group_details(
        "-33rd-chesscom-quick-knockouts-1401-1600", 1, 1
    )
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_team_match(12803)
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_team_match_board(12803, 1)
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_team_match_live(5833)
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_team_match_live_board(5833, 1)
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_country_details("XE")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_country_players("XE")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_country_clubs("XE")
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_current_daily_puzzle()
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_random_daily_puzzle()
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_streamers()
    assert isinstance(data, ChessDotComResponse)

    data = endpoints.get_leaderboards()
    assert isinstance(data, ChessDotComResponse)


def test_endpoints_async():
    client = ChessDotComClient(
        aio=True, rate_limit_handler=RateLimitHandler(tts=4, retries=2)
    )

    usernames = ["fabianocaruana", "GMHikaruOnTwitch", "MagnusCarlsen", "GarryKasparov"]

    usernames_multiplied = usernames * 5

    cors = [client.get_player_profile(name) for name in usernames_multiplied]

    async def gather_cors(cors):
        responses = await asyncio.gather(*cors)
        return responses

    responses = asyncio.run(gather_cors(cors))

    assert all(isinstance(r, ChessDotComResponse) for r in responses)
    assert len(responses) == len(usernames_multiplied)
