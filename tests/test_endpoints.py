import sys
import asyncio

is_main = __name__ == "__main__"
if is_main:
    sys.path.append("../")

from chessdotcom import client
from chessdotcom import ChessDotComResponse

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

client.Client.request_config["headers"][
    "user-agent"
] = "chess.com wrapper testing scripts. Contact me at sarartur.ruk@gmail.com"


def test_endpoints():
    client.Client.aio = False

    data = client.get_player_profile("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_titled_players("GM")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_player_stats("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_player_current_games("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_player_current_games_to_move("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_player_game_archives("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_player_games_by_month(
        username="fabianocaruana", year="2020", month="05"
    )
    assert isinstance(data, ChessDotComResponse)

    data = client.get_player_games_by_month_pgn(
        username="fabianocaruana", year="2020", month="05"
    )
    assert isinstance(data, ChessDotComResponse)

    data = client.get_player_clubs("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_player_team_matches("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_player_tournaments("fabianocaruana")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_club_details("chess-com-developer-community")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_club_members("chess-com-developer-community")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_club_matches("chess-com-developer-community")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_tournament_details("-33rd-chesscom-quick-knockouts-1401-1600")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_tournament_round("-33rd-chesscom-quick-knockouts-1401-1600", 1)
    assert isinstance(data, ChessDotComResponse)

    data = client.get_tournament_round_group_details(
        "-33rd-chesscom-quick-knockouts-1401-1600", 1, 1
    )
    assert isinstance(data, ChessDotComResponse)

    data = client.get_team_match(12803)
    assert isinstance(data, ChessDotComResponse)

    data = client.get_team_match_board(12803, 1)
    assert isinstance(data, ChessDotComResponse)

    data = client.get_team_match_live(5833)
    assert isinstance(data, ChessDotComResponse)

    data = client.get_team_match_live_board(5833, 1)
    assert isinstance(data, ChessDotComResponse)

    data = client.get_country_details("XE")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_country_players("XE")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_country_clubs("XE")
    assert isinstance(data, ChessDotComResponse)

    data = client.get_current_daily_puzzle()
    assert isinstance(data, ChessDotComResponse)

    data = client.get_random_daily_puzzle()
    assert isinstance(data, ChessDotComResponse)

    data = client.get_streamers()
    assert isinstance(data, ChessDotComResponse)

    data = client.get_leaderboards()
    assert isinstance(data, ChessDotComResponse)


def test_endpoints_async():

    client.Client.aio = True

    client.Client.rate_limit_handler.retries = 2
    client.Client.rate_limit_handler.tts = 4

    usernames = ["fabianocaruana", "GMHikaruOnTwitch", "MagnusCarlsen", "GarryKasparov"]

    usernames_multiplied = usernames * 5

    cors = [client.get_player_profile(name) for name in usernames_multiplied]

    async def gather_cors(cors):
        responses = await asyncio.gather(*cors)
        return responses

    responses = asyncio.run(gather_cors(cors))

    assert all(isinstance(r, ChessDotComResponse) for r in responses)
    assert len(responses) == len(usernames_multiplied)

    return responses


if is_main:
    test_endpoints()
    data = test_endpoints_async()
