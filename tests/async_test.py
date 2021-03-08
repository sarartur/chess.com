import sys
sys.path.append("../")
from datetime import datetime

from chessdotcom.aio import *
from chessdotcom import ChessDotComResponse
from asyncio import gather, get_event_loop
from datetime import datetime


def test_endpoints(print_ = False, break_ = False):

    Client.config['headers']['user-agent'] = 'chess.com wrapper testing scripts. Contact me at saradzhyanartur@gmail.com'

    cors = []

    cors.append(get_player_profile("fabianocaruana"))
    cors.append(get_player_stats("fabianocaruana"))
    cors.append(is_player_online("fabianocaruana"))
    cors.append(get_player_current_games("fabianocaruana"))
    cors.append(get_player_current_games("fabianocaruana"))
    cors.append(get_player_current_games_to_move("fabianocaruana"))
    cors.append(get_player_game_archives("fabianocaruana"))
    cors.append(get_player_games_by_month(username = "fabianocaruana", year='2020', month='05'))
    cors.append(get_player_games_by_month_pgn(username = "fabianocaruana", year='2020', month='05'))
    cors.append(get_player_clubs("fabianocaruana"))
    cors.append(get_player_team_matches("fabianocaruana"))
    cors.append(get_player_tournaments("fabianocaruana"))
    cors.append(get_club_details("chess-com-developer-community"))
    cors.append(get_club_members("chess-com-developer-community"))
    cors.append(get_club_matches("chess-com-developer-community"))
    cors.append(get_tournament_details("-33rd-chesscom-quick-knockouts-1401-1600"))
    cors.append(get_tournament_round("-33rd-chesscom-quick-knockouts-1401-1600", 1)) 
    cors.append(get_tournament_round_group_details("-33rd-chesscom-quick-knockouts-1401-1600", 1, 1)) 
    cors.append(get_team_match(12803))
    cors.append(get_team_match_board(12803, 1))
    cors.append(get_team_match_live(5833))
    cors.append(get_team_match_live_board(5833, 1))
    cors.append(get_country_details('XE'))
    cors.append(get_country_players('XE'))
    cors.append(get_country_clubs('XE'))
    cors.append(get_current_daily_puzzle())
    cors.append(get_random_daily_puzzle())
    cors.append(get_streamers())
    cors.append(get_leaderboards())

    return Client.loop.run_until_complete(gather(*cors))


if __name__ == "__main__":
    start = datetime.now()
    test_endpoints()
    end = datetime.now()
    print(end - start)
    for result in test_endpoints():
        print(result)
        input()



